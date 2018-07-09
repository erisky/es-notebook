## WiFi Related Commands

List the frequent used wifi commands

* [Radio](#radio)
    * channel 
    * tx power
    * bandwidth
* SSID
    * 
* STAs
* Neighbor 


### Radio

* Channel
    -  List of supported channels   
    ``` iwlist ath1 channel ```  
    
    -  Channge channel by command   
    ``` iwconfig ath1 channel 100 ```  

    - Get current channel width  
    ```iwpriv ath1 get_chwidth    ```   
       0: 20MHZ   
       1: 40 MHZ    
       2: 80 MHZ    
       3: 80_80/160MHZ    
        
* Mode
    - Get Current Operation Mode  
    ``` iwpriv ath0 get_mode  ```

* TX Power
    - Set TX power by dbm  
    ``` iwconfig ath0 txpower 21 ```

    


### Qualcomm (Atheros) Wifi commands
```
 80211stats athstats athstatsclr apstats pktlogconf pktlogdump wifitool wlanconfig thermaltool wps_enhc exttool assocdenialnotify

```



