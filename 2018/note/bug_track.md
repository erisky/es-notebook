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



### Wlan TX power emmission issue
* Phenomenon:  
    EAO3402P board rev2 back, no wlan tx is detected.
* root cause:  
    GPIO43 is pulled high in this version and it affected wireles tx.
* solution:  
    modifies dts file to switch the function from **wireless lte coexist** to normal gpio

```diff
-                                       function="wifi_wci1";
+                                       /*function="wifi_wci1"; */
+                                       function="gpio";

@@ -95,6 +96,22 @@
                                        output-high;
                                };
                        };

+                       sfp_pins: sfp_pinmux {
+                               mux {
+                    /* gpio 43 is left unchanged above*/
+                                       pins = "gpio42", "gpio44", "gpio45", "gpio46", "gpio47", "gpio48";
+                                       function="gpio";
+                                       bias-none;
+                               };
+                       };
+                       hwver_pins: hwver_pinmux {
+                               mux {
+                                       pins = "gpio49", "gpio50", "gpio68";
+                                       function="gpio";
+                                       bias-none;
+                               };
+                       };
+



```


### Template
* Phenomenon:  
* Root cause:  
* Solution:  



