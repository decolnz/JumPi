from subprocess import Popen, PIPE

#python-pip is needed to install sh via PIP for myIP.py
#python-dev is required
#Screen for consoling to routers/switches
#MOSH for mobile shell connectivity
#openswan and xl2tpd for L2TP/IPsec (VPN)
#openvpn for non-L2TP/IPsec (VPN)
Popen('apt-get install python-pip python-dev screen mosh openswan xl2tpd openvpn', shell=True, stdin=PIPE).communicate("y")

#installs sh via pip
Popen('pip install sh', shell=True, stdin=None, stdout=None).wait()

#copies ipchange bash script to dhcp-exit-hooks so it runs on IP assignment
Popen('cp /home/pi/JumPi/scripts/ipchange /etc/dhcp/dhclient-exit-hooks.d', shell=True, stdin=None, stdout=None).wait()

print "\nDon't forget to configure btsync!"
