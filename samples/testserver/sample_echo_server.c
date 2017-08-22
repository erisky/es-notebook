#include "uv.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <assert.h>

#ifdef UV_IPC_PIPE
#define USE_PIPE  (1)
#else
#define USE_PIPE  (0)
#endif
#define ASSERT assert

#define FATAL printf

typedef struct {
	uv_write_t req;
	uv_buf_t buf;
} write_req_t;

static void
alloc_buffer(uv_handle_t * handle, size_t suggested_size, uv_buf_t * buf)
{
	buf->base = malloc(suggested_size);
	buf->len = suggested_size;
}

static void on_close(uv_handle_t * peer)
{
	free(peer);
}

static void after_shutdown(uv_shutdown_t * req, int status)
{
	uv_close((uv_handle_t *) req->handle, on_close);
	free(req);
}

static void after_write(uv_write_t * req, int status)
{
	write_req_t *wr;

	/*
	 * Free the read/write buffer and the request 
	 */
	wr = (write_req_t *) req;
	free(wr->buf.base);
	free(wr);

	if (status == 0)
		return;

	fprintf(stderr,
		"uv_write error: %s - %s\n",
		uv_err_name(status), uv_strerror(status));
}

static void echo_read(uv_stream_t * handle, ssize_t nread, const uv_buf_t * buf)
{
	int i;
	write_req_t *wr;
	uv_shutdown_t *sreq;

#if 1
	printf("nread:%d\n", (int) nread);
#else

	if (nread < 0) {
		/*
		 * Error or EOF 
		 */
		ASSERT(nread == UV_EOF);

		free(buf->base);
		sreq = malloc(sizeof *sreq);
		ASSERT(0 == uv_shutdown(sreq, handle, after_shutdown));
		return;
	}
#endif
	if (nread < 0) {
		free(buf->base);
		sreq = malloc(sizeof *sreq);
		uv_shutdown(sreq, handle, after_shutdown);
		return;
	}
	if (nread == 0) {
		/*
		 * Everything OK, but nothing read. 
		 */
		free(buf->base);
		return;
	}
	/*
	 * Scan for the letter Q which signals that we should quit the server.
	 * If we get QS it means close the stream.
	 */
	if (strncmp(buf->base, "quit", 4) == 0) {
		uv_close((uv_handle_t *) handle, on_close);
		return;
	}

	wr = (write_req_t *) malloc(sizeof *wr);
	ASSERT(wr != NULL);
	wr->buf = uv_buf_init(buf->base, nread);

	if (uv_write(&wr->req, handle, &wr->buf, 1, after_write)) {
		FATAL("uv_write failed");
	}
}

void on_new_connection(uv_stream_t * server, int status)
{
	if (status < 0) {
		fprintf(stderr, "New connection error %s\n",
			uv_strerror(status));
		// error!
		return;
	}
#if USE_PIPE			//domain_socket
	uv_pipe_t *client = (uv_pipe_t *) malloc(sizeof(uv_pipe_t));
	uv_pipe_init(uv_default_loop(), client, 1);
#else
	uv_tcp_t *client = (uv_tcp_t *) malloc(sizeof(uv_tcp_t));
	uv_tcp_init(uv_default_loop(), client);
#endif
	if (uv_accept(server, (uv_stream_t *) client) == 0) {
		uv_read_start((uv_stream_t *) client, alloc_buffer, echo_read);
	} else {
		uv_close((uv_handle_t *) client, NULL);
	}
}

#if USE_PIPE			

uv_connect_t connect_req;
int main()
{
	int r;
	uv_loop_t *loop;
	uv_pipe_t pipe_server;
	uv_pipe_t pipe_client;
	char buf[128];
	size_t len = 128;
	loop = uv_default_loop();
	char *domain_file = "/var/tmp/pipe.server1";
	/* 1. Init */
	uv_pipe_init(loop, &pipe_server, 1);
	/* 2. bind */
	printf("%s\n", domain_file);

	unlink(domain_file);
	r = uv_pipe_bind(&pipe_server, domain_file);

	if (r != 0) {
		printf("bind error \n");

	}

	r = uv_pipe_getsockname(&pipe_server, buf, &len);
	if (r == 0) {
		printf("name =  %s \n", buf);
	}
	/* 3. listen */
	r = uv_listen((uv_stream_t *) & pipe_server, 0, on_new_connection);

	if (r) {
		fprintf(stderr, "Listen error %s\n", uv_strerror(r));
		return 1;
	}
	return uv_run(loop, UV_RUN_DEFAULT);
}
#else
int main()
{

	static uv_loop_t *loop;
	struct sockaddr_in addr;
	int port = 4789;
	loop = uv_default_loop();

	uv_tcp_t server;
	uv_tcp_init(loop, &server);

	uv_ip4_addr("0.0.0.0", port, &addr);

	uv_tcp_bind(&server, (const struct sockaddr *)&addr, 0);
	int r = uv_listen((uv_stream_t *) & server, 1024, on_new_connection);
	if (r) {
		fprintf(stderr, "Listen error %s\n", uv_strerror(r));
		return 1;
	}
	return uv_run(loop, UV_RUN_DEFAULT);
}

#endif
