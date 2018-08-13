## WPS and wifi SON ##



## Hotplug:  ##
* Trace :

add in  /sbin/hotplug-call 
```
[ -c /dev/console ] && echo "ACTION=$ACTION" > /dev/console
[ -c /dev/console ] && echo "HOTPLUG_TYPE=$HOTPLUG_TYPE" > /dev/console
[ -c /dev/console ] && echo "BUTTON=$BUTTON" > /dev/console
```

1. if sta interface exists, /lib/wifi/wpa_supplicant.sh create the control interface by 

>  wpa_cli -g /var/run/wpa_supplicantglobal interface_add  $ifname /var/run/wpa_supplicant-$ifname.conf $dr
> ls /var/run/wpa_supplicant...


2. to enable wps:
> Button pressed  call to /etc/hotplug.d/button/52-wps-supplicant

* no action when  /var/run/son_active exists  
     --> when son_active, this button is processed by son -->  to /var/run/sonwps.pipe

* if sta not connected 
     wpa_cli -p<<iface_ctrl create in 1. >> wps_pbc
     wpa_cli -p<<iface_ctrl create in 1. >> -a/lib/wifi/wps-supplicant-update-uci -P$pid -B


* wps-supplicant-update-uci updates uci when wps ends
 end codes:
    CONNECTED: update ssid/encryption/key etc..
    WPS-TIMEOUT:  call hotplug to inform wps-timeout ?
    DISCONNECTED ==> ?? should not happen



> qca prgoraming chapter 12.4  sucks
   


## WPA Supplicant 

**Collecte in  macsec.md**


