1> Build fw with tcpdump feature enabled

2> Configure your wifi monitor interfaces to "monitor mode" and restart wifi manually
   Ex- 
       // Set wifi0-wifi3 to monitor mode
       uci set wireless.wifi0.disabled='0'
       uci set wireless.wifi1.disabled='0'
       uci set wireless.wifi2.disabled='0'
       uci set wireless.@wifi-iface[0].mode='monitor'
       uci set wireless.@wifi-iface[1].mode='monitor'
       uci set wireless.@wifi-iface[2].mode='monitor'
       uci commit wireless

       wifi // restart wifi

3> Configure the channel you which you want to sniffer
   Ex-
       /* take chater board for example,
          we set ath0 (5G intf) on channel 161 */

       ifconfig ath0 down
       iwconfig ath0 channel 161
       ifconfig ath0 up

4> Then, we can capture packets from local or remote pc now.

Local - (capture and store on device)

       //on console terminal
       mkdir /tmp/sniffer
       tcpdump -i ath0 -s 0 -w /tmp/sniffer/2g_capture.pcapng -G 1800 -C 100 -K -n &

Remote - (capture from your pc, it can do real time monitor)

       PS: you need to enable ssh feature on device first

       //on your pc terminal
       ssh root@192.168.1.1 "tcpdump -i ath0 -s 0 -K -n -w -" | wireshark -k -i -

       Then, you can monitor the wireless packet from your pc site.
       You also can set filter. Ex: "wlan.fc.subtype==8" will only see the beacon packets

