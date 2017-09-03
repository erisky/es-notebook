#include <stdio.h>
#include <stdlib.h>
#include <string.h>
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
    session_item_t *ptmp = malloc(sizeof (session_item_t));
    ptmp->id = id;
    strcpy(ptmp->name, name);

    return ptmp;
}

#define REVERSE_ORDER (0)
int session_item_cmp(session_item_t *ptmp1 , session_item_t *ptmp2)
{
#if REVERSE_ORDER
    return ptmp2->id - ptmp1->id ;
#else    
    return ptmp1->id - ptmp2->id ;
#endif    
}


int session_item_cmp_id(session_item_t *ptmp1 , int id)
{
    if (ptmp1->id == id) 
        return 0;
    return 1;
}

int main() {
    session_item_t *head, *item;
    session_item_t local;
    int i, max = 100;
    head = new_item(0, "HEAD");

    for (i = 1; i < max ; i++) {
        char temp[32];
        sprintf(temp,"item%d",i);
        item = new_item(i,temp);
        LL_APPEND(head, item);
    }

    for (i = max; i < 2* max ; i++) {
        char temp[32];
        sprintf(temp,"item%d",i);
        item = new_item(i,temp);
        LL_PREPEND(head, item);
    }



    i = 0;
    LL_FOREACH(head, item) {
        printf("%d -> %d\n", i, item->id);
        i++;

    }
    local.id = 23;
    LL_SEARCH(head, item, &local, session_item_cmp);

    if (item) {
        printf("delete item:%d -> %d(%s)\n", i, item->id, item->name);
        LL_DELETE(head, item);
    }
   
    LL_SEARCH(head, item, 78, session_item_cmp_id);
    if (item) {
        printf("delte item:%d -> %d(%s)\n", i, item->id, item->name);
        LL_DELETE(head, item);
    } 
    LL_COUNT(head, item, i);
    printf("list count = %d\n", i);

#if 1    
    LL_SORT(head, session_item_cmp);
    i = 0;
    LL_FOREACH(head, item) {
        printf("%d -> %d\n", i, item->id);
        i++;

    }

#endif

}
 


