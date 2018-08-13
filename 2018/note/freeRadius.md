## FreeRadius Installation and setup

* get free radius server 
```
 $ cd ~/git/freeradius/
  get freeradius-server-release_3_0_16.tar.gz and extract
 $ cd freeradius-server-release_3_0_16/
 $ ./configure
 $ sudo apt-get install libhiredis
 $ make 
 $ sudo make install
```

- edit /usr/local/etc/raddb/radiusd.conf

```
    allow_vulnerable_openssl = yes  ## because we uses openssl with old version and there is a hole

```
- edit /usr/local/etc/raddb/mods-available/eap

```
    default_eap_type = peap         ## 802.11i doens't allow md5, 
                                    ## make this the default (eap-pwd was commented )
```

- edit /usr/local/etc/raddb/clients.conf

```
        ipv4addr = *            # any.  127.0.0.1 == localhost
        secret = testing123     ## Secret between AP and Radius Server
    
```
- edit /usr/local/etc/raddb/mods-config/files/authorize

```
## from the top of this file
## user and password
bob     Cleartext-Password := "hello123"
        Reply-Message := "Hello, %{User-Name}" 
```


###  Certificate 
* regnerate certificates

```
cd /usr/local/etc/raddb/certs/
rm -f *.pem *der *csr *.crt *.key *.p12 serial* index.txt*
./bootstrap 

```

* Using EAP on Android phone

- First is to install CA certificate 
> Get previously generate files (ca.pem) and install to android phone

 ==> so PEAP or EAP-TTLS is ok

 But fail to install client certificate 

 ==> so EAP-TLS is not working .... or not working on android phone







