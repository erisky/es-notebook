
# DBUS Study

## Reference
- https://en.wikipedia.org/wiki/D-Bus
- https://dbus.freedesktop.org/doc/dbus-tutorial.html
- https://www.freedesktop.org/wiki/IntroductionToDBus/


## Basic

- C binding: libdbus or A more practical C binding is based on GLib

-  Both one-to-one messaging and publish/subscribe communication are supported.

- A bus address will typically be the filename of a Unix-domain socket such as "/tmp/.hiddensocket,"

- 2 bus daemon:
    - started using the **dbus-launch** command
    - System bus
        /etc/dbus-1/system.conf
        ubuntu ==> find  /etc/dbus-1/system.d/
    - Sesson bus
        /etc/dbus-1/session.conf
        ubuntu ==> find  /etc/dbus-1/session.d/  ==> nothing !?
    - Configuration files are in a simple XML-based format called **busconfig**

- Bus Model 
    valid bus name is like:  org.freedesktop.NetworkManager
    unique connection name: given when to a connection to a bus, not reused in bus life cycle, ex: :1.1553
    bus names : a process ask from bus daemon: can be reused


     
￼
In D-Bus, a process offers its services exposing objects


A process connected to a D-Bus bus can request it to export as many D-Bus objects as it wants.

Each object is identified by an object path
[object path] example : /org/kde/kspread/sheets/3/cells/4/5

 in order to be able to use a certain service, a client must indicate not only the object path providing the desired service, but also the bus name under which the service process is connected to the bus

 [object-path + bus name]

Members : methods and signals
interface : a set of declarations of methods

 A D-Bus object can implement several interfaces, but at least must implement one, 


