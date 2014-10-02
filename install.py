from subprocess import Popen, PIPE

#installs PIP, which is needed to install sh for myIP.py
Popen('apt-get install python-pip', shell=True, stdin=PIPE).communicate("y")

#installs python-dev, which is needed for various commands to work
Popen('apt-get install python-dev', shell=True, stdin=PIPE).communicate("y")

#installs Screen so we can connect to console on routers/switches
Popen('apt-get install screen', shell=True, stdin=PIPE).communicate("y")

#installs MOSH
Popen('apt-get install mosh', shell=True, stdin=PIPE).communicate("y")

#installs openswan for L2TP VPN connectivity
#Popen('apt-get install openswan', shell=True, stdin=PIPE).communicate("y")

#installs sh via pip
Popen('pip install sh', shell=True, stdin=None, stdout=None)

#copies ipchange bash script
Popen('cp /home/pi/JumPi/scripts/ipchange /etc/dhcp/dhclient-exit-hooks.d', shell=True, stdin=None, stdout=None)

print "\nDon't forget to configure btsync!"
