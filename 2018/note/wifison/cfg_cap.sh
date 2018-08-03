echo > /etc/config/wireless << EOF
config wifi-device  wifi0
        option type     qcawificfg80211
        option channel  auto
        option macaddr  1c:b0:44:39:96:d1
        option hwmode   11axa
        option htmode   HT80
        # REMOVE THIS LINE TO ENABLE WIFI:
        option disabled 0

config wifi-iface wla
        option device   wifi0
        option network  lan
        option mode     ap
        option ssid     OpenWrt
        option encryption none

config wifi-device  wifi1
        option type     qcawificfg80211
        option channel  auto
        option macaddr  1c:b0:44:39:96:d0
        option hwmode   11axg
        # REMOVE THIS LINE TO ENABLE WIFI:
        option disabled 0

config wifi-iface wlg
        option device   wifi1
        option network  lan
        option mode     ap
        option ssid     OpenWrt
        option encryption none
EOF


uci set lbd.@config[0].Enable=1
uci set repacd.repacd.Enable=1
uci set hyd.@config[0].Enable=1
uci set wsplcd.repacd.Enable=1
uci commit lbd
uci commit repacd
uci commit hyd
uci commit wsplcd



# Configure the CAP according to 11
uci set wireless.@wifi-iface[0].ssid=Wifison123
uci set wireless.@wifi-iface[0].encryption=psk2+ccmp
uci set wireless.@wifi-iface[0].key=1234567890

# Configure ath0 as a backhaul --> allow RE to connect

uci set wireless.@wifi-iface[0].backhaul=1
uci set wireless.@wifi-iface[0].wnm=1

### ath

# SSID
uci set wireless.wlg.ssid=Wifison123
uci set wireless.wlg.encryption=psk2+ccmp

#SSID key
uci set wireless.wlg.key=1234567890
uci set wireless.wlg.backhaul=1
uci set wireless.wlg.wnm=1


uci commit wireless



uci set wsplcd.config.HyFiSecurity=1

# log debug
uci set wsplcd.config.WriteDebugLogToFile=APPEND

uci set wsplcd.config.DebugLevel=DEBUG

uci commit wsplcd


uci set hyd.Topology.ENABLE_NOTIFICATION_UNICAST=1

uci set hyd.Topology.PERIODIC_QUERY_INTERVAL=15

uci commit hyd


uci set repacd.repacd.Enable=1
uci set repacd.repacd.ConfigREMode=son

uci set repacd.WiFiLink.DaisyChain=1
uci commit repacd
/etc/init.d/repacd start


