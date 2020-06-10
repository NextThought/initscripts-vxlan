Place these scripts in `/etc/sysconfig/network-scripts` on your
RedHat/CentOS/Fedora system.

Sample configuration for a `vxlan` interface associated with a specific interface and has learning disabled:

	TYPE=vxlan
	DEVICE=vxlan1000
	BOOTPROTO=none
	ONBOOT=yes
	TTL=255
	VNI=1000
	DSTPORT=4789
	LOCAL_ADDR="192.168.1.1"
	PHYS_DEV="eth0"
	OPTIONS="nolearning"
	BRIDGE="br1000"

Sample configuration for a `vxlan` interface that lets the kernel determine the output interface and uses static flooding to distribute BUM packets.:

	TYPE=vxlan
	DEVICE=vxlan1000
	BOOTPROTO=none
	ONBOOT=yes
	TTL=255
	VNI=1000
	DSTPORT=4789
	LOCAL_ADDR="192.168.1.1"
	REMOTE_VTEPS="192.168.1.2 192.168.1.3 192.168.1.4"
	BRIDGE="br1000"

Additional information on using VXLAN on Linux can be found at https://vincent.bernat.ch/en/blog/2017-vxlan-linux
