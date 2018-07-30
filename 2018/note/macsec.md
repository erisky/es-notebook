
## MACSEC study


## Module

## Source 
> ~/spf5_test/eao3402p/spf5/qualcomm_sdk/qsdk/build_dir/target-arm_cortex-a7_uClibc-1.0.14_eabi/qca-hostap-10.4-supplicant-macsec/qca-hostap-spf50

> qsdk/qca/src/qca-hostap-10.4



## Hostapd
* Configuration 
* Initilization 
- entry
  hostapd_global_ctrl_iface_init  
- eloop register  
> hostapd_global_ctrl_iface_receive

hostapd_global_ctrl_iface_receive
 :: control interface : 
 --> "ADD"
> hostapd_ctrl_iface_add  
> hostapd_add_iface  
> hostapd_config_alloc


- Start from install driver
> hostapd_config_alloc


wpa-driver:  
wpa_driver_ops wpa_driver_nl80211_ops

nl80211_global_init
wpa_driver_nl80211_init_nl_global


* Control
- hostapd_cli :
- Users:
/etc/hotplug.d/button/50-wps
/lib/wifi/qcawifi.sh
/lib/wifi/wps-hostapd-update-uci
/lib/wifi/wps-supplicant-update-uci
/lib/wifi/hostapd.sh



## WPA supplicant

/usr/sbin/wpa_cli -> control to the hostapd or ?



## Related RFCs

- RFC 2284 - PPP Extensible Authentication Protocol (EAP) x --> 3748
- RFC 2716 - PPP EAP TLS Authentication Protocol 
- RFC 2865 - Remote Authentication Dial In User Service (RADIUS)   *
- RFC 2139 - RADIUS Accounting
- RFC 2869 - RADIUS Extensions *
- RFC 3162 - RADIUS and IPv6
- RFC 3575 - IANA Considerations for RADIUS  
- RFC 3579 - RADIUS Support For Extensible Authentication Protocol
- RFC 3580 - IEEE 802.1X RADIUS Usage Guidelines
- RFC 3748 - Extensible Authentication Protocol (EAP)
- RFC 4072 - Diameter Extensible Authentication Protocol (EAP) Application
- RFC 4186 - Extensible Authentication Protocol Method for GSM SIM
- RFC 4675 - RADIUS Attributes for Virtual LAN and Priority Support
- RFC 5090 - RADIUS Extension for Digest Authentication 
- RFC 5176 - Dynamic Authorization Extensions to RADIUS
- RFC 5247 - Extensible Authentication Protocol (EAP) Key Management Framework

- RFC 6613 -  RADIUS over TCP 
- RFC 6614 - Transport Layer Security (TLS) Encryption for RADIUS
- RFC 6911 - RADIUS Attributes for IPv6 Access Networks 

- RFC 6929 -  Remote Authentication Dial-In User Service (RADIUS)
                          Protocol Extensions


- RFC 7268 - RADIUS Attributes for IEEE 802 Networks

