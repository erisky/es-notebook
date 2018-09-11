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

# 	compatible = "gpio-leds"; is must when adding new mux to dts 



```


### SFP Module is not working on EAO3402P 
* Phenomenon:  
  
* Root cause:  
    Not setup correctly
* Solution:  
   1. Bootstraping need to setup 
      if no strap-pin reworked, even link is up but no packets are found
   2. gpio45 must set up 
      note: in querying qca why gpio43 and gpio45 is swapped  

   ```
    echo 45 > /sys/class/gpio/export 
    echo out > /sys/class/gpio/gpio45/direction
   ```  

    3. phy register must be setup to select fiber combo
    ```
    dev0@qca>debug phy set 4 31 0x0503
    
    ```

* known issue:
    1. link is only 10
    2. no idea how to setup combo at intial without bootstrap
    3. once the iper started, eth0 tx packets are not sent out 
    4. auto-detect the spf module is possible, but it's not possible to detect 
       the sfp module link status and speed ... etc


```
port interfaceMode set  5 psgmii_amdet
port mediumType get 5
>> get gpio  then ok
```


### Template
* Phenomenon:  
* Root cause:  
* Solution:  



