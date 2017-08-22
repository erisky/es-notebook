/*
 * file protocol headers
 */
#include <stdio.h>
#define FSS_MAX_FILENAME_LEN (256)
#define FSS_FILE_CHECKSUM_LEN (32)

//256 MB
#define FSS_MAX_FILE_SIZE   (256*1024*1024)

enum file_server_state_e {
    FSS_NONE,
    FSS_CONNECTED,
    FSS_HEADER_READY,   // req ok, before send resp
    FSS_WAIT_START,     // wait client start 
    FSS_TRANSFER,       // transfering 
    FSS_DONE,           // done
    FSS_ERROR,
};

struct per_session_file_info {
    enum file_server_state_e state;
    char filename[FSS_MAX_FILENAME_LEN];
    int filesize;
    char checksum[FSS_FILE_CHECKSUM_LEN];
    FILE *fp;
};


#define FSS_HSK_HDR_SIZE (8)
#define FSS_MAGIC (0x98AC0000)
#define FSS_FILE_REQ   (FSS_MAGIC | 1)
#define FSS_FILE_RESP_OK    (FSS_MAGIC | 2)
#define FSS_FILE_RESP_ERROR (FSS_MAGIC | 3)
#define FSS_FILE_START      (FSS_MAGIC | 4)
#define FSS_DUMMY           (FSS_MAGIC | 0xF)

#define FSS_GET_MAGIC(x)    (x & 0xffff0000)


struct fss_header_hsk {
    int  type;
    int  filesize;
    char checksum[FSS_FILE_CHECKSUM_LEN];
    char filename[FSS_MAX_FILENAME_LEN];  
   
};

/*
 * Client only
 * */
enum file_client_state_e {
    FSC_NONE,
    FSC_CONNECTED,
    FSC_WAIT_CONFIRM,     // wait server confirm 
    FSC_CONFIRMED,      //received ok from server
    FSC_TRANSFER,       // transfering 
    FSC_DONE,           // done
    FSC_ERROR,
};


struct per_session_file_client_info {
    enum file_client_state_e state;
    char filename[FSS_MAX_FILENAME_LEN];
    int filesize;
    int bytes;
    char checksum[FSS_FILE_CHECKSUM_LEN];
    FILE *outfp;
};



extern int
callback_file_server(struct lws *wsi, enum lws_callback_reasons reason,
			void *user, void *in, size_t len);

int 
callback_file_client(struct lws *wsi, enum lws_callback_reasons reason,
			void *user, void *in, size_t len);

