#!/bin/sh

wrapd -P /var/run/wrapd-global.pid -g /var/run/wrapdglobal -H /var/run/hostapd/global -w /var/run/wpa_supplicantglobal -b br-lan -i eth1 -l 20 -t 1 -e 1-r 1 &

wrapd -P /var/run/wrapd-global.pid -g /var/run/wrapdglobal -H /var/run/hostapd/global -w /var/run/wpa_supplicantglobal -b br-lan -i eth0 -l 20 -t 1 -e 1 -r 1 -a
wrapd -P /var/run/wrapd-global.pid -g /var/run/wrapdglobal -H /var/run/hostapd/global -w /var/run/wpa_sup
#       wrapd -S -g /var/run/wrapd-wifiX -L
wrapd -S -g /var/run/wrapd-wifi0 -L
wrapd -S -g /var/run/wrapdglobal -L
wrapd -S -g /var/run/wrapdglobal -A F0:03:8C:07:64:57  (NB WIFI)


wrapd -S -g /var/run/wrapdglobal -A 84:16:f9:06:f2:2f  (PC)

# Disable wifi1
uci set wireless.wifi0.disabled=0
uci set wireless.wifi1.disabled=1
uci set wireless.wifi2.disabled=0


uci set wireless.wifi0.qwrap_enable=1
uci set wireless.wifi2.qwrap_enable=1

uci commit dhcp

# Disable dhcp and uses static IP
uci set dhcp.lan.ignore=1
uci commit dhcp
uci set network.lan.ifname='eth0 eth1'
uci set network.lan.proto=static
uci set network.lan.ipaddr=192.168.1.78
uci set network.lan.gateway=192.168.1.2
uci set network.lan.dns=192.168.1.2


#uci set wireless.wifi0.disabled=


uci set wireless.@wifi-iface[0].mode=wrap
uci set wireless.@wifi-iface[0].ssid='EC_TEST_2G'
uci set wireless.@wifi-iface[0].encryption=psk2+ccmp
uci set wireless.@wifi-iface[0].key='12345678'
uci set wireless.@wifi-iface[0].wpa_group_rekey=2000
uci set wireless.@wifi-iface[0].device=wifi0
uci set wireless.@wifi-iface[0].network=lan
uci set wireless.@wifi-iface[0].extender_device=wifi0



uci add wireless wifi-iface
uci set wireless.@wifi-iface[3].mode=sta
uci set wireless.@wifi-iface[3].device=wifi0
uci set wireless.@wifi-iface[3].network=lan
uci set wireless.@wifi-iface[3].encryption=psk2+ccmp
uci set wireless.@wifi-iface[3].key='12345678'
uci set wireless.@wifi-iface[3].wpa_group_rekey=2000
uci set wireless.@wifi-iface[3].ssid='EC_3RD_AP'
uci commit wireless
uci export wireless
wifi


SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ

[Using Repacd start]
>>> Config <<<
config wifi-device 'wifi0'
        option type 'qcawifi'
        option channel 'auto'
        option macaddr 'b4:ee:b4:e9:89:07'
        option hwmode '11ng'
        option disabled '0'
        option qwrap_dbdc_enable '1'
        option dbdc_enable '1'

config wifi-iface
        option device 'wifi0'
        option network 'lan'
        option mode 'ap'
        option backhaul_ap '1'
        option ssid 'whc-E98905'
        option wps_pbc '1'
        option wps_pbc_enable '1'
        option wps_pbc_start_time '0'
        option wps_pbc_duration '120'
        option encryption 'psk2+ccmp'
        option key 'ZQEzqG50+G4='
        option disabled '0'
        option wds '0'
        option qwrap_ap '1'
        option blockdfschan '1'
        option rrm '0'
        option extap '0'
        option root_distance '255'
        option athnewind '0'

config wifi-device 'wifi1'
        option type 'qcawifi'
        option channel 'auto'
        option macaddr '00:34:56:78:5e:5e'
        option hwmode '11ac'
        option disabled '0'
        option qwrap_enable '1'
        option dbdc_enable '1'

config wifi-iface
        option device 'wifi1'
        option network 'lan'
        option backhaul_ap '1'
        option ssid 'whc-E98905'
        option wps_pbc '1'
        option wps_pbc_enable '1'
        option wps_pbc_start_time '0'
        option wps_pbc_duration '120'
        option encryption 'psk2+ccmp'
        option key 'ZQEzqG50+G4='
        option disabled '0'
        option wds '0'
        option qwrap_ap '1'
        option mode 'wrap'
        option blockdfschan '1'
        option rrm '0'
        option extap '0'
        option root_distance '255'
        option athnewind '0'

config wifi-device 'wifi2'
        option type 'qcawifi'
        option channel 'auto'
        option macaddr 'b4:ee:b4:e9:89:06'
        option hwmode '11ac'
        option disabled '0'
        option qwrap_enable '1'
        option dbdc_enable '1'

config wifi-iface
        option device 'wifi2'
        option network 'lan'
        option backhaul_ap '1'
        option ssid 'whc-E98905'
        option wps_pbc '1'
        option wps_pbc_enable '1'
        option wps_pbc_start_time '0'
        option wps_pbc_duration '120'
        option encryption 'psk2+ccmp'
        option key 'ZQEzqG50+G4='
        option disabled '0'
        option wds '0'
        option qwrap_ap '1'
        option mode 'wrap'
        option blockdfschan '1'
        option rrm '0'
        option extap '0'
        option root_distance '255'
        option athnewind '0'

config qcawifi 'qcawifi'
        option wps_pbc_extender_enhance '1'
        option wps_pbc_overwrite_ap_settings_all '1'

config wifi-iface
        option device 'wifi0'
        option network 'lan'
        option ssid 'whc-E98905'
        option wps_pbc '1'
        option wps_pbc_enable '1'
        option wps_pbc_start_time '0'
        option wps_pbc_duration '120'
        option encryption 'psk2+ccmp'
        option key 'ZQEzqG50+G4='
        option mode 'sta'
        option disabled '1'
        option wds '0'
        option extap '0'
        option root_distance '255'
        option athnewind '0'

config wifi-iface
        option device 'wifi1'
        option network 'lan'
        option ssid 'whc-E98905'
        option wps_pbc '1'
        option wps_pbc_enable '1'
        option wps_pbc_start_time '0'
        option wps_pbc_duration '120'
        option encryption 'psk2+ccmp'
        option key 'ZQEzqG50+G4='
        option mode 'sta'
        option disabled '0'
        option wds '0'
        option extap '0'
        option root_distance '255'
        option athnewind '0'

config wifi-iface
        option device 'wifi2'
        option network 'lan'
        option ssid 'whc-E98905'
        option wps_pbc '1'
        option wps_pbc_enable '1'
        option wps_pbc_start_time '0'
        option wps_pbc_duration '120'
        option encryption 'psk2+ccmp'
        option key 'ZQEzqG50+G4='
        option mode 'sta'
        option disabled '0'
        option wds '0'
        option extap '0'
        option root_distance '255'
        option athnewind '0'



wrapd -P /var/run/wrapd-global.pid -g /var/run/wrapdglobal -H /var/run/hostapd/global -w /var/run/wpa_supplicantglobal -b br-lan -i eth0 -l 20 -t 1 -e 1 -r 1 -a

wireless.wifi0=wifi-device
wireless.wifi0.type='qcawifi'
wireless.wifi0.channel=1
wireless.wifi0.macaddr='b4:ee:b4:e9:89:07'
wireless.wifi0.hwmode='11ng'
wireless.wifi0.disabled='0'
wireless.wifi0.qwrap_dbdc_enable='0'
wireless.wifi0.dbdc_enable='0'
wireless.@wifi-iface[0]=wifi-iface
wireless.@wifi-iface[0].device='wifi0'
wireless.@wifi-iface[0].network='lan'
wireless.@wifi-iface[0].mode='wrap'
#wireless.@wifi-iface[0].backhaul_ap='1'
wireless.@wifi-iface[0].ssid='EC_QWRAP'
#wireless.@wifi-iface[0].wps_pbc='1'
#wireless.@wifi-iface[0].wps_pbc_start_time='0'
#wireless.@wifi-iface[0].wps_pbc_duration='120'
wireless.@wifi-iface[0].encryption='psk2+ccmp'
wireless.@wifi-iface[0].key='12345678'
wireless.@wifi-iface[0].disabled='0'
wireless.@wifi-iface[0].extap='0'
wireless.@wifi-iface[0].athnewind='0'
wireless.@wifi-iface[0].wps_pbc_enable='0'
wireless.@wifi-iface[0].wds='0'
wireless.@wifi-iface[0].qwrap_ap='1'
wireless.@wifi-iface[0].blockdfschan='0'
wireless.@wifi-iface[0].rrm='1'
wireless.@wifi-iface[0].root_distance='0'
wireless.wifi1=wifi-device
wireless.wifi1.type='qcawifi'
wireless.wifi1.channel='auto'
wireless.wifi1.macaddr='00:34:56:78:5e:5e'
wireless.wifi1.hwmode='11ac'
wireless.wifi1.qwrap_enable='0'
wireless.wifi1.dbdc_enable='0'
wireless.wifi1.disabled='1'
wireless.@wifi-iface[1]=wifi-iface
wireless.@wifi-iface[1].device='wifi1'
wireless.@wifi-iface[1].network='lan'
wireless.@wifi-iface[1].backhaul_ap='1'
wireless.@wifi-iface[1].ssid='whc-E98905'
wireless.@wifi-iface[1].wps_pbc='1'
wireless.@wifi-iface[1].wps_pbc_start_time='0'
wireless.@wifi-iface[1].wps_pbc_duration='120'
wireless.@wifi-iface[1].encryption='psk2+ccmp'
wireless.@wifi-iface[1].key='ZQEzqG50+G4='
wireless.@wifi-iface[1].disabled='1'
wireless.@wifi-iface[1].extap='0'
wireless.@wifi-iface[1].athnewind='0'
wireless.@wifi-iface[1].wps_pbc_enable='0'
wireless.@wifi-iface[1].wds='1'
wireless.@wifi-iface[1].qwrap_ap='0'
wireless.@wifi-iface[1].mode='ap'
wireless.@wifi-iface[1].blockdfschan='0'
wireless.@wifi-iface[1].rrm='1'
wireless.@wifi-iface[1].root_distance='0'
wireless.wifi2=wifi-device
wireless.wifi2.type='qcawifi'
wireless.wifi2.channel=36
wireless.wifi2.macaddr='b4:ee:b4:e9:89:06'
wireless.wifi2.hwmode='11ac'
wireless.wifi2.disabled='0'
wireless.wifi2.qwrap_enable='1'
#wireless.wifi2.dbdc_enable='1'
wireless.@wifi-iface[2]=wifi-iface
wireless.@wifi-iface[2].device='wifi2'
wireless.@wifi-iface[2].network='lan'
wireless.@wifi-iface[2].backhaul_ap='1'
wireless.@wifi-iface[2].ssid='123'
wireless.@wifi-iface[2].wps_pbc='1'
wireless.@wifi-iface[2].wps_pbc_start_time='0'
wireless.@wifi-iface[2].wps_pbc_duration='120'
wireless.@wifi-iface[2].encryption='psk2+ccmp'
wireless.@wifi-iface[2].key='ZQEzqG50+G4='
wireless.@wifi-iface[2].disabled='0'
wireless.@wifi-iface[2].extap='0'
wireless.@wifi-iface[2].athnewind='0'
wireless.@wifi-iface[2].wps_pbc_enable='0'
wireless.@wifi-iface[2].wds='1'
wireless.@wifi-iface[2].qwrap_ap='0'
wireless.@wifi-iface[2].mode='ap'
wireless.@wifi-iface[2].blockdfschan='0'
#wireless.@wifi-iface[2].rrm='1'
wireless.@wifi-iface[2].root_distance='0'
wireless.qcawifi=qcawifi
#wireless.qcawifi.wps_pbc_overwrite_ap_settings_all='1'
#wireless.qcawifi.wps_pbc_extender_enhance='0'
wireless.@wifi-iface[3]=wifi-iface
wireless.@wifi-iface[3].device='wifi0'
wireless.@wifi-iface[3].network='lan'
wireless.@wifi-iface[3].ssid='whc-E98905'
wireless.@wifi-iface[3].wps_pbc='1'
wireless.@wifi-iface[3].wps_pbc_start_time='0'
wireless.@wifi-iface[3].wps_pbc_duration='120'
wireless.@wifi-iface[3].encryption='psk2+ccmp'
wireless.@wifi-iface[3].key='ZQEzqG50+G4='
wireless.@wifi-iface[3].mode='sta'
wireless.@wifi-iface[3].disabled='1'
wireless.@wifi-iface[3].extap='0'
wireless.@wifi-iface[3].athnewind='0'
wireless.@wifi-iface[3].wps_pbc_enable='0'
wireless.@wifi-iface[3].wds='1'
wireless.@wifi-iface[3].root_distance='0'
wireless.@wifi-iface[4]=wifi-iface
wireless.@wifi-iface[4].device='wifi1'
wireless.@wifi-iface[4].network='lan'
wireless.@wifi-iface[4].ssid='whc-E98905'
wireless.@wifi-iface[4].wps_pbc='1'
wireless.@wifi-iface[4].wps_pbc_start_time='0'
wireless.@wifi-iface[4].wps_pbc_duration='120'
wireless.@wifi-iface[4].encryption='psk2+ccmp'
wireless.@wifi-iface[4].key='ZQEzqG50+G4='
wireless.@wifi-iface[4].mode='sta'
wireless.@wifi-iface[4].extap='0'
wireless.@wifi-iface[4].athnewind='0'
wireless.@wifi-iface[4].wps_pbc_enable='0'
wireless.@wifi-iface[4].disabled='1'
wireless.@wifi-iface[4].wds='1'
wireless.@wifi-iface[4].root_distance='0'
wireless.@wifi-iface[5]=wifi-iface
wireless.@wifi-iface[5].device='wifi2'
wireless.@wifi-iface[5].network='lan'
wireless.@wifi-iface[5].ssid='whc-E98905'
wireless.@wifi-iface[5].wps_pbc='1'
wireless.@wifi-iface[5].wps_pbc_start_time='0'
wireless.@wifi-iface[5].wps_pbc_duration='120'
wireless.@wifi-iface[5].encryption='psk2+ccmp'
wireless.@wifi-iface[5].key='ZQEzqG50+G4='
wireless.@wifi-iface[5].mode='sta'
wireless.@wifi-iface[5].extap='0'
wireless.@wifi-iface[5].athnewind='0'
wireless.@wifi-iface[5].wps_pbc_enable='0'
wireless.@wifi-iface[5].disabled='1'
wireless.@wifi-iface[5].wds='1'
wireless.@wifi-iface[5].root_distance='0'


XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

uci show wireless

uci set wireless.wifi0=wifi-device
uci set wireless.wifi0.type='qcawifi'
uci set wireless.wifi0.channel='auto'
#uci set wireless.wifi0.macaddr='b4:ee:b4:e9:89:07'
uci set wireless.wifi0.hwmode='11ng'
uci set wireless.wifi0.disabled='0'
uci set wireless.wifi0.qwrap_dbdc_enable='1'
uci set wireless.wifi0.dbdc_enable='1'
uci set wireless.@wifi-iface[0]=wifi-iface
uci set wireless.@wifi-iface[0].device='wifi0'
uci set wireless.@wifi-iface[0].network='lan'
uci set wireless.@wifi-iface[0].mode='wrap'
#wireless.@wifi-iface[0].backhaul_ap='1'
uci set wireless.@wifi-iface[0].ssid='EC_WRAP'
#wireless.@wifi-iface[0].wps_pbc='1'
#wireless.@wifi-iface[0].wps_pbc_start_time='0'
#wireless.@wifi-iface[0].wps_pbc_duration='120'
uci set wireless.@wifi-iface[0].encryption='psk2+ccmp'
uci set wireless.@wifi-iface[0].key='12345678'
uci set wireless.@wifi-iface[0].disabled='0'
uci set wireless.@wifi-iface[0].extap='0'
uci set wireless.@wifi-iface[0].athnewind='0'
uci set wireless.@wifi-iface[0].wps_pbc_enable='0'
uci set wireless.@wifi-iface[0].wds='0'
uci set wireless.@wifi-iface[0].qwrap_ap='1'
#wireless.@wifi-iface[0].blockdfschan='0'
#wireless.@wifi-iface[0].rrm='1'
#wireless.@wifi-iface[0].root_distance='0'

uci set wireless.@wifi-iface[1]=wifi-iface
uci set wireless.@wifi-iface[1].device='wifi0'
uci set wireless.@wifi-iface[1].network='lan'
#wireless.@wifi-iface[1].backhaul_ap='1'
uci set wireless.@wifi-iface[1].ssid='EC_3RD_AP'
#wireless.@wifi-iface[1].wps_pbc='1'
#wireless.@wifi-iface[1].wps_pbc_start_time='0'
#wireless.@wifi-iface[1].wps_pbc_duration='120'
uci set wireless.@wifi-iface[1].encryption='psk2+ccmp'
uci set wireless.@wifi-iface[1].key='12345678'
uci set wireless.@wifi-iface[1].disabled='0'
uci set wireless.@wifi-iface[1].extap='0'
#wireless.@wifi-iface[1].athnewind='0'
#wireless.@wifi-iface[1].wps_pbc_enable='0'
#uci set wireless.@wifi-iface[1].wds='0'
#uci set wireless.@wifi-iface[1].qwrap_ap='1'
uci set wireless.@wifi-iface[1].mode='sta'
#uci set wireless.@wifi-iface[1].blockdfschan='0'
#uci set wireless.@wifi-iface[1].rrm='1'
#uci set wireless.@wifi-iface[1].root_distance='0'

### Disable wifi1
uci set wireless.wifi1=wifi-device
uci set wireless.wifi1.type='qcawifi'
uci set wireless.wifi1.channel='auto'
#uci set wireless.wifi1.macaddr='00:34:56:78:5e:5e'
uci set wireless.wifi1.hwmode='11ac'
uci set wireless.wifi1.qwrap_enable='0'
uci set wireless.wifi1.dbdc_enable='0'
uci set wireless.wifi1.disabled='1'

### wifi2 for 5G
uci set wireless.wifi2=wifi-device
uci set wireless.wifi2.type='qcawifi'
uci set wireless.wifi2.channel='auto'
#uci set wireless.wifi2.macaddr='b4:ee:b4:e9:89:06'
uci set wireless.wifi2.hwmode='11ac'
uci set wireless.wifi2.disabled='0'
uci set wireless.wifi2.qwrap_enable='1'
uci set wireless.wifi2.dbdc_enable='0'
uci set wireless.@wifi-iface[2]=wifi-iface
uci set wireless.@wifi-iface[2].device='wifi2'
uci set wireless.@wifi-iface[2].network='lan'
#uci set #wireless.@wifi-iface[2].backhaul_ap='1'
uci set wireless.@wifi-iface[2].ssid='EC_WRAP'
#uci set #wireless.@wifi-iface[2].wps_pbc='1'
#uci set #wireless.@wifi-iface[2].wps_pbc_start_time='0'
#uci set #wireless.@wifi-iface[2].wps_pbc_duration='120'
uci set wireless.@wifi-iface[2].encryption='psk2+ccmp'
uci set wireless.@wifi-iface[2].key='12345678'
uci set wireless.@wifi-iface[2].disabled='0'
uci set wireless.@wifi-iface[2].extap='0'
uci set wireless.@wifi-iface[2].athnewind='0'
#uci set #wireless.@wifi-iface[2].wps_pbc_enable='0'
uci set wireless.@wifi-iface[2].wds='0'
uci set wireless.@wifi-iface[2].qwrap_ap='1'
uci set wireless.@wifi-iface[2].mode='wrap'
#uci set #wireless.@wifi-iface[2].blockdfschan='0'
#uci set #wireless.@wifi-iface[2].rrm='1'
uci set wireless.@wifi-iface[2].root_distance='0'
uci set wireless.qcawifi=qcawifi

uci add wireless wifi-iface
#uci set #wireless.qcawifi.wps_pbc_overwrite_ap_settings_all='1'
#uci set #wireless.qcawifi.wps_pbc_extender_enhance='0'
uci set wireless.@wifi-iface[3]=wifi-iface
uci set wireless.@wifi-iface[3].device='wifi2'
uci set wireless.@wifi-iface[3].network='lan'
uci set wireless.@wifi-iface[3].ssid='EC_3RD_AP'
#uci set #wireless.@wifi-iface[3].wps_pbc='1'
#uci set #wireless.@wifi-iface[3].wps_pbc_start_time='0'
#uci set #wireless.@wifi-iface[3].wps_pbc_duration='120'
uci set wireless.@wifi-iface[3].encryption='psk2+ccmp'
uci set wireless.@wifi-iface[3].key='12345678'
uci set wireless.@wifi-iface[3].mode='sta'
#uci set wireless.@wifi-iface[3].disabled='0'
#uci set wireless.@wifi-iface[3].extap='0'
#uci set #wireless.@wifi-iface[3].athnewind='0'
#uci set #wireless.@wifi-iface[3].wps_pbc_enable='0'
#uci set wireless.@wifi-iface[3].wds='0'
#uci set wireless.@wifi-iface[3].root_distance='0'

uci commit 