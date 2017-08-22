#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/time.h>
#include "uthash/utlist.h"

struct session_item_s {
	int id;
	char name[32];
	struct session_item_s *next;
};

typedef struct session_item_s session_item_t;

//session_item_t *list = NULL:

session_item_t *new_item(int id, char *name)
{
	session_item_t *ptmp = malloc(sizeof(session_item_t));
	ptmp->id = id;
	strcpy(ptmp->name, name);

	return ptmp;
}

#define REVERSE_ORDER (0)
int session_item_cmp(session_item_t * ptmp1, session_item_t * ptmp2)
{
#if REVERSE_ORDER
	return ptmp2->id - ptmp1->id;
#else
	return ptmp1->id - ptmp2->id;
#endif
}

int session_item_cmp_id(session_item_t * ptmp1, int id)
{
	if (ptmp1->id == id)
		return 0;
	return 1;
}

#include <stdlib.h>
#include <stdio.h>
#include "uthash/uthash.h"

/* example: ip/port/ac mac*/
typedef struct {
    int ip;
	int port;
    char acmac[6];
} session_key_t;


typedef struct {
    char mac[6];
} client_key_t;


// HASH_ADD
// HASH_ADD         (hh_name, head, keyfield_name, key_len, item_ptr)
// HASH_FIND        (hh_name, head, key_ptr, key_len, item_ptr)
// HASH_REPLACE     (hh_name, head, keyfield_name, key_len, item_ptr, replaced_item_ptr)
// HASH_DEL
// HASH_ITER
typedef struct {
	session_key_t key;
    char text[320];
	/* ... other data ... */
	UT_hash_handle hh;
} record_t;


#define UT_BENCH_TOTAL_RECORDS  (1000000)
#define MORE_REC_NUM            (1000)

static struct timeval tv_rec;
void _start_measure(void)
{
    gettimeofday(&tv_rec, NULL);
    //printf("start time:%d, us:%d\n", tv.tv_sec, tv.tv_usec);
}

//return the us elasped
int _stop_measure(void)
{
    struct timeval tv;
    int ret;

    gettimeofday(&tv, NULL);
    ret = (tv.tv_sec - tv_rec.tv_sec ) * 1000000 + (tv.tv_usec - tv_rec.tv_usec);
    
    //printf("start time:%d, us:%d\n", tv.tv_sec, tv.tv_usec);
    return ret;
}



int main(int argc, char *argv[])
{
	record_t l, *p, *r, *tmp, *records = NULL;
    int i,x,found,elapse_us;
    struct timeval tv;
       
    srand(time(NULL));
    //srand(1234);

    _start_measure();
    for ( x = 0; x< UT_BENCH_TOTAL_RECORDS; x++) {
       	r = (record_t *) malloc(sizeof(record_t));
       	memset(r, 0, sizeof(record_t));
#if 0
       	r->key.ip =  i++;
       	r->key.port = i++;

#else        
       	r->key.ip = rand();
       	r->key.port = rand() & 0xffff;
#endif        
        r->key.acmac[0] = 0xa1;        
        sprintf(r->text, "t%d %d ", x,x);

#if 1        
        HASH_FIND(hh, records, &r->key, sizeof(session_key_t), p);
        if (!p)
#endif            
           	HASH_ADD(hh, records, key, sizeof(session_key_t), r);
    }
    elapse_us = _stop_measure();
    printf("done adding %d records in %d us \n",UT_BENCH_TOTAL_RECORDS, elapse_us );
    _start_measure();
    for (x = 0; x < MORE_REC_NUM; x++) {    
   	    r = (record_t *) malloc(sizeof(record_t));
   	    memset(r, 0, sizeof(record_t));
   	    r->key.ip = 0xcaa0a001+x;
   	    r->key.port =  2345+x;
        r->key.acmac[0] = 0xa2;
        sprintf(r->text, "Find me:%d !! ",x);
   	    HASH_ADD(hh, records, key, sizeof(session_key_t), r);
    }
    elapse_us = _stop_measure();
    printf("done adding %d more records in %d us\n",MORE_REC_NUM, elapse_us);
    printf("HASH_COUNT:%d\n", HASH_COUNT(records));

    //gettimeofday(&tv, NULL);
    //printf("start time:%d, us:%d\n", tv.tv_sec, tv.tv_usec);

	memset(&l, 0, sizeof(record_t));
	l.key.ip = 0x12321231;
	l.key.port = 1231;
    l.key.acmac[0] = 0xa1;
	HASH_FIND(hh, records, &l.key, sizeof(session_key_t), p);

    
	if (p) {
        printf("found %x %d --> %s \n", p->key.ip, p->key.port, p->text);
    }
    else {
        //printf("not found\n");
    }


    found = 0;
    _start_measure();
    for (x = 0; x < MORE_REC_NUM; x++) {    
	    memset(&l, 0, sizeof(record_t));
    	l.key.ip = 0xcaa0a001+x;
	    l.key.port = 2345+x;
        l.key.acmac[0] = 0xa2;
	    HASH_FIND(hh, records, &l.key, sizeof(session_key_t), p);
        if (p) {
            //printf("%s\n", p->text);
            found ++;        
        }
    }
    elapse_us = _stop_measure();
    printf("found items:%d in %d us\n", found, elapse_us);
	if (p) {
	    printf("found %x %d --> %s \n", p->key.ip, p->key.port, p->text);
	   	r = (record_t *) malloc(sizeof(record_t));
    	r->key.ip = 0xcaa0a001;
       	r->key.port =  2345;
        r->key.acmac[0] = 0xa2;
        sprintf(r->text, "NEW VALUE");
        HASH_REPLACE (hh, records, key, sizeof(session_key_t), r, p);
        if (p) {
            printf("replaced:%s", p->text);            
            free(p);
        }

    }
    else {
        printf("not found\n");
    }

    gettimeofday(&tv, NULL);
    printf("end time:%d, us:%d\n", tv.tv_sec, tv.tv_usec);


    /*delete 1000 for testing */
    i = 0;
    x = 0;
    _start_measure();
	HASH_ITER(hh, records, p, tmp) {
        i++;
        //printf("%s %x %d\n", p->text, p->key.ip, p->key.port);
        if ( (i&1) == 1) {
            x++;
		    HASH_DEL(records, p);
		    free(p);
        }
        if (x >= MORE_REC_NUM)
            break;
	}
    elapse_us = _stop_measure();
    printf("delete %d items in %d us\n", x, elapse_us);


    _start_measure();
    x = 0;
	HASH_ITER(hh, records, p, tmp) {
        x++;
        //printf("%s %x %d\n", p->text, p->key.ip, p->key.port);
		HASH_DEL(records, p);
		free(p);
	}
    elapse_us = _stop_measure();
    printf("deleted x=%d in %d us\n", x, elapse_us);
	return 0;
}
