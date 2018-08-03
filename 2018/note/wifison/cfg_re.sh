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
uci set repacd.repacd.Enable=1          ### NO such UCI !?
uci set hyd.@config[0].Enable=1
uci set wsplcd.repacd.Enable=1
uci commit lbd
uci commit repacd
uci commit hyd
uci commit wsplcd


uci set network.lan.proto=dhcp
uci delete network.wan
uci commit network

/etc/init.d/network restart
/etc/init.d/dnsmasq restart
uci set wireless.@wifi-iface[0].backhaul_ap=1
uci set wireless.@wifi-iface[1].backhaul_ap=1
uci set wireless.wifi1.ul_hyst=10   # Optional: Hysteresis for best uplink node selection. 10 = 10% of Max PHY rate (default value if
                                    # no value is set). The configuration assumes that wifi1 is the radio
                                    # with the 5 GHz STA interface.
uci commit wireless
uci set hyd.Topology.ENABLE_NOTIFICATION_UNICAST=1 #Optional: set if using RootAP
uci set hyd.Topology.PERIODIC_QUERY_INTERVAL=15 #Optional: set if using RootAP
uci commit hyd
uci set wsplcd.config.HyFiSecurity=1

uci set wsplcd.config.WriteDebugLogToFile=APPEND

uci set wsplcd.config.DebugLevel=DEBUG
uci commit wsplcd;
uci set repacd.repacd.Enable=1
uci set repacd.WiFiLink.DaisyChain=1
uci set repacd.repacd.ConfigREMode=son
uci set repacd.repacd.DefaultREMode=son
uci set repacd.WiFiLink.ManageVAPInd=1
# Set this for
# independent repeater mode. If backhaul STA interfaces go down -AP
# interfaces will also go down if this is set to 0.
uci commit repacd
/etc/init.d/repacd start
uci set wsplcd.config.HyFiSecurity=1

