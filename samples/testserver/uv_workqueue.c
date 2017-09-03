#include "uv.h"

#define FIB_UNTIL (4)
uv_loop_t *loop;

int fib_(int n)
{
	if (n == 0)
		return 0;
	if (n == 1)
		return 1;
	return fib_(n - 1) + fib_(n - 2);
}

uv_async_t async;
void fib(uv_work_t * req)
{
	int n = *(int *)req->data;

	sleep(random() % 3 + 1);

	async.data = n * 8;
	uv_async_send(&async);
	sleep(1);
	long fib = fib_(n);
	fprintf(stderr, "%dth fibonacci is %lu\n", n, fib);
}

void after_fib(uv_work_t * req, int status)
{
	fprintf(stderr, "Done calculating %dth fibonacci\n", *(int *)req->data);
}

void print_progress(uv_async_t * handle)
{
	int n = (int)handle->data;
	fprintf(stderr, "got data:%d\n", n);

}

int main()
{
	loop = uv_default_loop();

	int data[FIB_UNTIL];
	uv_work_t req[FIB_UNTIL];
	int i;

	uv_async_init(loop, &async, print_progress);

	for (i = 0; i < FIB_UNTIL; i++) {
		data[i] = i;
		req[i].data = (void *)&data[i];
		uv_queue_work(loop, &req[i], fib, after_fib);
	}

	return uv_run(loop, UV_RUN_DEFAULT);
}
