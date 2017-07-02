#include <stdio.h>
#include "postgreConfig.h"


int main(int argc, char *argv[])
{
    int x = 9;

    printf("Release version: %d.%d \n",postgre_VERSION_MAJOR, postgre_VERSION_MINOR);
    printf("If this work\n");

#ifdef HAVE_PRINTF
    printf("Printf is available\n");
#else
    exit(-1);
#endif

#ifdef USE_MYSQRT
    printf("MY SQRT:%d = %d", x, my_sqrt(x));
#else
    printf("MY SQRT: not defined\n");
#endif
}
