#include <stdio.h>
#include "TutorialConfig.h"

#ifdef USE_MYSQRT
#include "my_sqrt.h"
#endif

int main(int argc, char *argv[])
{
    int x = 9;

    printf("Release version: %d.%d \n",Tutorial_VERSION_MAJOR, Tutorial_VERSION_MINOR);
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
