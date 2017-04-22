
--------------- learning 1
iwpriv ath0 get_wds 
#wlanconfig ath0 nawds mode 2    #
wlanconfig ath0 nawds mode 4     # learning bridge
wlanconfig  ath0 nawds defcaps 0x501
wlanconfig  ath0 nawds list
#wlanconfig ath0 nawds add-repeater B4:EE:B4:E9:89:06 0x501
wlanconfig ath0 hmwds read-table
wlanconfig ath0 hmwds dump-wdstable


#wait peer
wlanconfig  ath0 nawds list
wlanconfig ath0 hmwds read-table
wlanconfig ath0 hmwds dump-wdstable


--------------- static 1
iwpriv ath0 get_wds 
wlanconfig  ath0 nawds list
wlanconfig ath0 nawds mode 2
wlanconfig  ath0 nawds defcaps 0x501
wlanconfig  ath0 nawds list
wlanconfig ath0 hmwds read-table
wlanconfig ath0 hmwds dump-wdstable
wlanconfig ath0 nawds add-repeater B4:EE:B4:E9:89:06 0x501
wlanconfig  ath0 nawds list
wlanconfig ath0 hmwds read-table
wlanconfig ath0 hmwds dump-wdstable








---------------- static 2
iwpriv ath0 get_wds 
wlanconfig  ath0 nawds list
wlanconfig ath0 nawds mode 2
wlanconfig  ath0 nawds defcaps 0x501
wlanconfig  ath0 nawds list
wlanconfig ath0 hmwds read-table
wlanconfig ath0 hmwds dump-wdstable
 wlanconfig ath0 nawds add-repeater  00:03:7F:12:83:83  0x501
wlanconfig  ath0 nawds list
wlanconfig ath0 hmwds read-table
wlanconfig ath0 hmwds dump-wdstable

 



