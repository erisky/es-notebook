/*
 * our own file protocol
 *
 */
#include "test-server.h"
#include "test-server-file.h"




int 
callback_file_client(struct lws *wsi, enum lws_callback_reasons reason,
			void *user, void *in, size_t len)
{

	unsigned char buf[LWS_PRE + 4096];
	struct per_session_file_client_info *psc =
			(struct per_session_file_client_info *)user;
    struct fss_header_hsk  *phsk;
    int n;

    //printf("reason:%d\n", reason);
	switch (reason) {
	case LWS_CALLBACK_CLIENT_ESTABLISHED:

		lwsl_notice("FSC: LWS_CALLBACK_CLIENT_ESTABLISHED\n");
        psc->state = FSC_CONNECTED;
        
        /* only write when writable */
		lws_callback_on_writable(wsi);
		break;

	case LWS_CALLBACK_CLOSED:
		lwsl_notice("FSC: Closed");
		break;

    case LWS_CALLBACK_CLIENT_WRITEABLE:
        if (psc->state == FSC_CONNECTED) {
            memset(buf, 0, 1000);
            phsk = (struct fss_header_hsk  *) &buf[0];
            phsk->filesize = 1;
            phsk->type = FSS_FILE_REQ ;
            n = lws_write(wsi, (unsigned char*) phsk, sizeof(struct fss_header_hsk), LWS_WRITE_BINARY );
            if (n<sizeof(struct fss_header_hsk)) {
			    lwsl_err("FSC Write header failed\n");
                return -1;
            }

            psc->state = FSC_WAIT_CONFIRM;
            printf("confirm state\n");
        }
        else if (psc->state == FSC_CONFIRMED) {
            char filename[32];
            phsk = (struct fss_header_hsk  *) &buf[0];
                phsk->filesize = 1;
                sprintf(filename,"testout%d.bin", time(NULL));
                psc->outfp = fopen(filename, "wb");
                if (!psc->outfp)
                    return -1;

                phsk->type = FSS_FILE_START ;
    
                n = lws_write(wsi, (unsigned char*) phsk, sizeof(struct fss_header_hsk), LWS_WRITE_BINARY);
                if (n<sizeof(struct fss_header_hsk)) {
			        lwsl_err("FSC Write header failed\n");
                    return -1;
                }

            psc->state = FSC_TRANSFER;
        }
        else {
            //send dummy 
            phsk = (struct fss_header_hsk  *) &buf[0];
            phsk->type = FSS_DUMMY;

           // n = lws_write(wsi, (unsigned char*) phsk, FSS_HSK_HDR_SIZE, LWS_WRITE_BINARY);
        }
		//lws_callback_on_writable(wsi);
		break;
    case LWS_CALLBACK_CLIENT_RECEIVE:
        if (psc->state == FSC_WAIT_CONFIRM) {
            phsk = (struct fss_header_hsk  *) in;
            printf("Rev:%08x\n", phsk->type);
            if (phsk->type == FSS_FILE_RESP_OK) {
                psc->state = FSC_CONFIRMED;                
            }
            else {
                printf("error, server reject\r\n");
                return -1;
            }
        }
        else if (psc->state == FSC_TRANSFER) {
            psc->bytes += len;
            printf("Got %d\n", (int)psc->bytes);
            fwrite(in, 1, len, psc->outfp);
            if (psc->bytes == 83762340) {
                printf("end\n");
                fclose(psc->outfp);
                exit(0);
                return -1;
            }
           //lws_callback_on_writable(wsi) ; // !?
     
        }
        else {
            printf("unexpected data got\r\n");            
        }
        lws_callback_on_writable(wsi);
        break;
	default:
        printf("unknown:%d \r\n", reason);
		break;
	}

	return 0;



}

int
callback_file_server(struct lws *wsi, enum lws_callback_reasons reason,
			void *user, void *in, size_t len)
{
	unsigned char buf[LWS_PRE + 10240];
	struct per_session_file_info *pss =
			(struct per_session_file_info *)user;
	unsigned char *p = &buf[LWS_PRE];
	int n, m;
    struct  fss_header_hsk *pHdr;

    int fd;
    char peername[128];
    char ip[32];
    struct sockaddr_storage addr; 
    struct sockaddr_in *s;  
    int port, slen;

	switch (reason) {

	case LWS_CALLBACK_ESTABLISHED:
        pss->state = FSS_CONNECTED;
        fd = lws_get_socket_fd(wsi);
        slen = sizeof addr;
        lws_get_peer_addresses(wsi, fd, peername, 128, ip, 32);
        getpeername(fd, (struct sockaddr*)&addr, &slen);
        s = (struct sockaddr_in *)&addr;
        port = ntohs(s->sin_port);
        printf("fs:%s (%s) port=%d connected\n", peername, ip, port);
		break;

	case LWS_CALLBACK_SERVER_WRITEABLE:
        if (pss->state == FSS_HEADER_READY) {
            pHdr = (struct fss_header_hsk*) &buf[LWS_PRE];
            pHdr->type = FSS_FILE_RESP_OK;
            printf("write header1\n");
            m = lws_write(wsi,(unsigned char*)pHdr, FSS_HSK_HDR_SIZE, LWS_WRITE_BINARY);
            if (m < FSS_HSK_HDR_SIZE) {
                lwsl_err("ERROR writing FSS Resp to socket \n");
    			return -1;    
            }
            pss->state = FSS_WAIT_START;
        }
        else if (pss->state == FSS_TRANSFER) {
            n = fread(buf, 1, 10000, pss->fp);            
            m = lws_write(wsi, buf, n, LWS_WRITE_BINARY);
            printf("sent:%d bytes\n",m);
            if (m < n) {
                lwsl_err("ERROR writing FILE Content to socket \n");
    			return -1;    
            }
 
            if (n < 10000) {
                printf("FSS_DONE\n");
                pss->state = FSS_DONE;
            }
            lws_callback_on_writable(wsi);
        }
        else if (pss->state == FSS_DONE){
            // server close socket

        }
		break;

	case LWS_CALLBACK_RECEIVE:
        if (pss->state == FSS_CONNECTED)  {
            printf("try to get file header!!");
            
            pHdr = (struct fss_header_hsk *) in;
            if ((FSS_GET_MAGIC(pHdr->type) != FSS_MAGIC )||
                (pHdr->filesize > FSS_MAX_FILE_SIZE)){
                pss->state = FSS_ERROR;
            }  
            else {
                strcpy(pss->filename, pHdr->filename);
                strcpy(pss->checksum, pHdr->checksum);
                pss->filesize = pHdr->filesize;
                pss->state = FSS_HEADER_READY; // 
            }
        }
        else if (pss->state == FSS_WAIT_START) {
                pss->fp = fopen("testfile.bin", "rb");
                if (pss->fp) {
                    pss->state = FSS_TRANSFER;
                } 
                else {
                    pss->state = FSS_ERROR;
                }
        }
        else {
            pHdr = (struct fss_header_hsk *) in;
            if (pHdr->type == FSS_DUMMY) {
                // ok
            }
            else {
                printf("unexpeced frame\n");
            }
        }



		break;
	/*
	 * this just demonstrates how to use the protocol filter. If you won't
	 * study and reject connections based on header content, you don't need
	 * to handle this callback
	 */
	case LWS_CALLBACK_FILTER_PROTOCOL_CONNECTION:
		//dump_handshake_info(wsi);
		/* you could return non-zero here and kill the connection */
		break;

	/*
	 * this just demonstrates how to handle
	 * LWS_CALLBACK_WS_PEER_INITIATED_CLOSE and extract the peer's close
	 * code and auxiliary data.  You can just not handle it if you don't
	 * have a use for this.
	 */
	case LWS_CALLBACK_WS_PEER_INITIATED_CLOSE:
		lwsl_notice("LWS_CALLBACK_WS_PEER_INITIATED_CLOSE: len %lu\n",
			    (unsigned long)len);
		for (n = 0; n < (int)len; n++)
			lwsl_notice(" %d: 0x%02X\n", n,
				    ((unsigned char *)in)[n]);
		break;

	default:
        printf("fsr, unknown reason:%d\r\n", reason);
		break;
	}

	return 0;
}
