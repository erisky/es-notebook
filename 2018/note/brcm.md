
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

~/spf5_test/test_eai2202p/spf5/qualcomm_sdk/qsdk
