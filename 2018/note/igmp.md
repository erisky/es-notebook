## IGMP Study

IGMP Study notes

### IGMP Versions



|             |     IGMPv1          | IGMPv2              | IGMPv3              |
|-------------|---------------------|---------------------|---------------------|
| Source-specifc multicast    | N   |  N                  | **Y**               |
| Default Query interval| 60s       |  125s               | 125s                |
| Leave group Msg|  N               |  Y                  | Y                   |
| Rtr send Grp-specifi Query |  N   |  Y                  | Y                   |
| Host send src/grp specific report |  N   |  N           | Y                   |
| Max rsp time configured? |  N,10s |  N                  | Y                   |



### Referece:

* [DeveloperWorks](https://www.ibm.com/developerworks/cn/linux/l-cn-igmp/ )


![kernel flow](file:///home/eric/work/note/es-notebook/2018/note/igmp/image006.jpg)



### Commands

> cat /proc/net/ip_mr_cache   
> cat /proc/net/ip_mr_vif

```bash
operator@EAI2204P:/etc/init.d# cat /proc/net/ip_mr_vif
Interface      BytesIn  PktsIn  BytesOut PktsOut Flags Local    Remote
 0 br-lan         2424      12      3237      21 00008 00000013 00000000
 1 eth0       75449388   55961         0       0 00008 0000000A 00000000
operator@EAI2204P:/etc/init.d# cat /proc/net/ip_mr_vif
Interface      BytesIn  PktsIn  BytesOut PktsOut Flags Local    Remote
 0 br-lan         2424      12      3237      21 00008 00000013 00000000
 1 eth0       75834492   56245         0       0 00008 0000000A 00000000

```


### Content for this document

* [Content1](#content1)
* [Order List](#Order-List)
    * [Subtarget](#subtarget)
        * subsubk?
* [Code Block](#Code-Block)

### Order List

