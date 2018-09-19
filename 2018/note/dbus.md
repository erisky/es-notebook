
# DBUS Study



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

- 

