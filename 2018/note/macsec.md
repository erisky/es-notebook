
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
- RFC 6613 - RADIUS over TCP 
- RFC 6614 - Transport Layer Security (TLS) Encryption for RADIUS
- RFC 6911 - RADIUS Attributes for IPv6 Access Networks 
- RFC 6929 - Remote Authentication Dial-In User Service (RADIUS) Protocol Extensions
- RFC 7268 - RADIUS Attributes for IEEE 802 Networks



## Macsec related files on EAX

* /etc/init.d/macsec restart
* /usr/sbin/wpa_supplicant -D macsec_qca -i "$ifname" -c /var/run/wpa_supplicant-macsec-$ifname.conf
  - macsec_qca : driver name
  - config name : 
* config @ 



## Related kernel message

[235179.329039] nss_macsec_secy_en_set[266]: error parameter!
[235179.333812] nss_macsec_secy_sc_sa_mapping_mode_set[155]: error parameter!
[235179.340832] nss_macsec_secy_rx_ctl_filt_set[65]: error parameter!
[235179.347008] nss_macsec_secy_tx_ctl_filt_set[204]: error parameter!
[235179.353462] nss_macsec_secy_controlled_port_en_set[175]: error parameter!
[235179.360268] nss_macsec_secy_controlled_port_en_set[175]: error parameter!
[235179.367123] nss_macsec_secy_controlled_port_en_set[175]: error parameter!
[235179.428835] nss_macsec_secy_en_set[266]: error parameter!
[235179.433533] nss_macsec_secy_rx_sc_del_all[332]: error parameter!
[235179.439712] nss_macsec_secy_tx_sc_del_all[550]: error parameter!
[235179.498514] nss_macsec_secy_en_set[266]: error parameter!
[235179.503279] nss_macsec_secy_sc_sa_mapping_mode_set[155]: error parameter!
[235179.510425] nss_macsec_secy_rx_ctl_filt_set[65]: error parameter!
[235179.516666] nss_macsec_secy_tx_ctl_filt_set[204]: error parameter!
[235179.523257] nss_macsec_secy_controlled_port_en_set[175]: error parameter!
[235179.531112] nss_macsec_secy_controlled_port_en_set[175]: error parameter!
[235179.540699] nss_macsec_secy_controlled_port_en_set[175]: error parameter!

* config file
 file path:
> /var/run/wpa_supplicant-macsec-eth0.conf

```
ctrl_interface=/var/run/wpa_supplicant-macsec-eth0
eapol_version=3
ap_scan=0
network={
        key_mgmt=IEEE8021X
        eap=MD5
        identity="eric"
        password="12345678"
        eapol_flags=0
        macsec_policy=1
}

```

## WPA supplicant notes

* Linux is moving to nl80211 ( -Dnl80211 on wpa_supplicant command line )
* Wired Ethernet drivers (with ap_scan=0)
* information: http://w1.fi/wpa_supplicant/devel/
* PDF: http://w1.fi/wpa_supplicant/wpa_supplicant-devel.pdf

https://www.cisco.com/c/en/us/products/collateral/ios-nx-os-software/identity-based-networking-services/deploy_guide_c17-663760.html



## MACSEC Intro
> https://www.cisco.com/c/en/us/products/collateral/ios-nx-os-software/identity-based-networking-services/deploy_guide_c17-663760.html


* MACsec was primarily designed to be used in conjunction with IEEE 802.1X-2010
* switch performs source MAC address filtering and port state monitoring to help ensure that only the authenticated endpoint is allowed to send traffic
* Before the 2010 revision of IEEE 802.1X,  rogue users with physical access to the authenticated port could monitor, modify, and send traffic
 - source MAC address filtering could be circumvented by MAC address spoofing.



## EAPol Flow

* 4-way handshake

   [Supplicate]                       [Autenticator]
        |
        | <---- [ EAPoL(Anounce...) ------- |  ....... wpa_receive ( src/ap/wpa_auth.c )
        | ----- [EAPoL(Snounce...)] ------> |                --> refer to standard section 11.6.2 for format
        | <---- [ EAPoL(Anounce,RSNE..)---- |
        | ----- [EAPoL(Snounce...)] ------> |


* 802.1x receive
    - Entry: ieee802_1x_receive (ap/ieee802_1x.c)
    - rules to drop packets: 
        - not from associated sta
        - too short
        - incorrect version
        - discard eapol if sta is psk ( goes to wpa_receive before this)

    - allocate ieee 802.1x state machine by ieee802_1x_alloc_eapol_sm
    - wps  (epa)
        

   [Supplicant]                                  [Autenticator]
        |
        | <-------- [ EAP Request (Indentity) ------------ |  
        | --------- [ EAP Response(Indentity=WFA)] ------> | .............
        | <-------- [ EAP Request (WPS WSC Start)]-------- |  
        | --------- [ EAP Response(WPS WSC Msg(M1))] ----> | 
        | <-------- [ EAP Request (WPS WSC Msg(M2))] ----- |  
        | --------- [ EAP Response(WPS WSC Msg(M3))] ----> | 
        | <-------- [ EAP Request (WPS WSC Msg(M4))] ----- |  
        | --------- [ EAP Response(WPS WSC Msg(M5))] ----> | 
        | <-------- [ EAP Request (WPS WSC Msg(M6))] ----- |  
        | --------- [ EAP Response(WPS WSC Msg(M7))] ----> | 
        | <-------- [ EAP Request (WPS WSC Msg(M8))] ----- |  
        | --------- [ EAP Response(WPS WSC Done)] -------> | 


code trace:
SM_STATE(EAP, METHOD)
eap_wsc_process



