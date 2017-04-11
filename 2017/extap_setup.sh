#!/bin/sh



#sed -i s/'option disabled 1'/'option disabled 0'/g /etc/config/wireless

# Disable wifi1
uci set wireless.wifi0.disabled=0
uci set wireless.wifi1.disabled=1
uci set wireless.wifi2.disabled=0

# Disable dhcp and uses static IP
uci set dhcp.lan.ignore=1
uci commit dhcp
uci set network.lan.ifname='eth0 eth1'
uci set network.lan.proto=static
uci set network.lan.ipaddr=192.168.1.78
uci set network.lan.gateway=192.168.1.2
uci set network.lan.dns=192.168.1.2


#uci set wireless.wifi0.disabled=


#interface 0:
uci set wireless.@wifi-iface[0].encryption='psk2+ccmp'
uci set wireless.@wifi-iface[0].disabled='0'
uci set wireless.@wifi-iface[0].wds='0'
uci set wireless.@wifi-iface[0].qwrap_ap='0'
uci set wireless.@wifi-iface[0].extap='1'
uci set wireless.@wifi-iface[0].ssid='EC_TEST_2G'
uci set wireless.@wifi-iface[0].key='12345678'

uci set wireless.@wifi-iface[2].encryption='psk2+ccmp'
uci set wireless.@wifi-iface[2].disabled='0'
uci set wireless.@wifi-iface[2].wds='0'
uci set wireless.@wifi-iface[2].qwrap_ap='0'
uci set wireless.@wifi-iface[2].extap='1'
uci set wireless.@wifi-iface[2].ssid='EC_TEST_5G'
uci set wireless.@wifi-iface[2].key='12345678'



## add interface ath01 in 'STA' mode for connecting
#uci add wireless wifi-iface
#uci set wireless.@wifi-iface[3]=wifi-iface
#uci set wireless.@wifi-iface[3].device='wifi0'
#uci set wireless.@wifi-iface[3].network='lan'
#uci set wireless.@wifi-iface[3].encryption='psk2+ccmp'
#uci set wireless.@wifi-iface[3].mode='sta'
#uci set wireless.@wifi-iface[3].wds='0'
#uci set wireless.@wifi-iface[3].extap='1'
#uci set wireless.@wifi-iface[3].root_distance='255'
#uci set wireless.@wifi-iface[3].athnewind='0'
#uci set wireless.@wifi-iface[3].ssid='EC_3RD_AP'
#uci set wireless.@wifi-iface[3].key='12345678'
#

echo "config wifi-iface
        option device 'wifi0'
        option network 'lan'
        option wps_pbc '1'
        option wps_pbc_enable '1'
        option wps_pbc_start_time '0'
        option wps_pbc_duration '120'
        option encryption 'psk2+ccmp'
        option mode 'sta'
        option wds '0'
        option extap '1'
        option root_distance '255'
        option athnewind '0'
        option ssid 'EC_3RD_AP'
        option key '12345678'" >> /etc/config/wireless



uci delete network.wan
uci commit network
/etc/init.d/dnsmasq restart	
/etc/init.d/network restart
