## Bug Tracking ##

### Veriwave performance
* Phenomenon:
  testing veriwave is not acheiveing the max performance 97x mbps.
* root cause:
  ebtable is enabled due to the usage of wifidog and skysoft_qos.
* solution:
  when ebtables is selected, it's added to AUTOLOAD so it's in modules.d which will be autoloaded at startup
  related files:
  - qsdk/include/netfilter.mk
  - qsdk/package/kernel/linux/modules/netfilter.mk
  - kmodloader.c (ubox)


