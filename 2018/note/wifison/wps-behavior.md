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
  
> ls /var/run/wpa_supplicant 



wpa_cli 


qca prgoraming chapter 12.4



* 
/etc/hotplug.d/button


