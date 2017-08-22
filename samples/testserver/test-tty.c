/* 
 *
 * */

#include "uv.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#ifdef UV_IPC_PIPE
#define USE_PIPE  (1)
#else
#define USE_PIPE  (0)
#endif


#if USE_PIPE
static uv_pipe_t client;
#else
static uv_tcp_t client;
#endif
static uv_tty_t tty;

typedef struct my_write_req_s {
	uv_write_t write_req;
	uv_buf_t buf;
} my_write_req_t;

static void write_cb(uv_write_t * req, int status);

static void
alloc_cb(uv_handle_t * handle, size_t suggested_size, uv_buf_t * buf)
{
	buf->base = malloc(suggested_size);
	buf->len = suggested_size;
}

//tty received 
static void recv_cb(uv_stream_t * handle, ssize_t nread, const uv_buf_t * buf)
{
	my_write_req_t *pmyWr = malloc(sizeof(my_write_req_t));

	pmyWr->buf = uv_buf_init(buf->base, nread);

	//write to tcp handle
	uv_write(&pmyWr->write_req, (uv_stream_t*)&client, &pmyWr->buf, 1, write_cb);

}

void on_close(uv_handle_t * handle)
{
	//free(handle);
	uv_stop(handle->loop);
}

static void
tcp_read_cb(uv_stream_t * handle, ssize_t nread, const uv_buf_t * buf)
{
	char temp[128];

	if (nread >= 0) {
		strncpy(temp, buf->base, nread);
		temp[nread] = 0;
		printf("%s (%d)", buf->base, (int)nread);
		free(buf->base);
	} else {
		uv_close((uv_handle_t*)handle, on_close);
	}
}

static void write_cb(uv_write_t * req, int status)
{
	my_write_req_t *myWr = (my_write_req_t *) req;
	/*
	 * Free the read/write buffer and the request 
	 */
	free(myWr);

	if (status == 0)
		return;

}

static void connect_cb(uv_connect_t * req, int status)
{

	int r;
	uv_stream_t *stream;

	stream = req->handle;

#if USE_PIPE
	printf("pipe connected....\n");
#else
	printf("tcp connected....\n");
#endif
	// do no write
	//r = uv_write(&pmyWr->write_req, stream, &pmyWr->buf, 1, write_cb);
	//printf("wr: r=%d\n",r);
	/* Start reading */
	r = uv_read_start(stream, alloc_cb, tcp_read_cb);
}

int main(void)
{
	uv_loop_t loop;

	struct sockaddr_in addr;
	uv_connect_t connect_req;

	int fd, r;

	/* loop init */
	uv_loop_init(&loop);

#if USE_PIPE
	uv_pipe_init(&loop, &client, 1);
	uv_pipe_connect(&connect_req, &client, "/var/tmp/pipe.server1",
			connect_cb);

#else
	/*tcp socket initial */
	uv_ip4_addr("127.0.0.1", 4789, &addr);

	uv_tcp_init(&loop, &client);

	uv_tcp_connect(&connect_req, &client,
		       (const struct sockaddr *)&addr, connect_cb);
#endif

	r = uv_tty_init(&loop, &tty, 0, 1);
	printf("r=%d\n", r);
	uv_read_start((uv_stream_t *) & tty, alloc_cb, recv_cb);

	uv_run(&loop, UV_RUN_DEFAULT);

	printf("end\n");
	return 0;
}
