
##Build Env


### Setenv
```bash
export LD_LIBRARY=/opt/toolchains/crosstools-arm-gcc-5.3-linux-4.1-glibc-2.24-binutils-2.25/usr/lib
export PATH=/projects/hnd/tools/linux/hndtools-armeabi-2011.09/bin:$PATH
export TOOLCHAIN_BASE=/opt/toolchains
## set default shell as bash
sudo dpkg-reconfigure dash

```


```bash
cd ~/wifi_project/
make PROFILE=94908HND

```

### Build DSL Project ###

* get file from \\10.194.20.21\d900-samba\public\Chipset\Broadcom\SW_DSL_Linux\5.02L.05\test5
* get toolchain from \\10.194.20.21\d900-samba\public\Chipset\Broadcom\SW_DSL_Linux\5.02L.05\test6
```
cd ~/work/broadcom/DSL/toolchain
tar jxvf crosstools-aarch64-gcc-5.3-linux-4.1-glibc-2.24-binutils-2.25.Rel1.9.tar.bz2
tar jxvf crosstools-arm-gcc-5.3-linux-4.1-glibc-2.24-binutils-2.25.Rel1.9.tar.bz2
```


* local working directory: ~/work/broadcom/DSL/test5

* get extract.sh from  \\10.194.20.21\d900-samba\private\charlesHsueh



* extract.sh
```
#!/bin/bash

ORIG_DIR=`pwd`

echo $ORIG_DIR
echo $1
echo $2

if [ ! -d $1 ]
then
	mkdir -p $1
fi

if [ ! -d $2 ]
then
	mkdir -p $2
fi

for i in ./b*.gz; do
	echo "Extracting file: " $i ":"
	tar xvf $i -C $1
	echo "done. to Next."
done

mkdir -p $1/image_files
mkdir -p $1/documentation

mv -v $1/*image*.gz $1/image_files
mv -v $1/*.pdf $1/documentation
mv -v $1/*.txt $1/documentation

echo "Listing the extracted file:"

ls -al $1
ls -al $1/image_files
ls -al $1/documentation

cd $1

for j in ./b*.gz; do
	echo "Extracting file: " $j ":"
	tar xvf $j -C $2
	echo "done. to Next."
done

echo "Listing the extracted file:"

ls -al $2

echo "Everything DONE. Exiting, Bye."

exit 0
```

* Run the script like
```
eric@eric-n809996:~/work/broadcom/DSL/test5$ ./extract.sh  ./ ../code/

```

* Build
```
cd ~/work/broadcom/DSL/code/cfe/build/broadcom/bcm63xx_rom


```


