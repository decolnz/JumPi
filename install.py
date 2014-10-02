from subprocess import Popen

#installs PIP, which is needed to install sh for myIP.py
Popen(['apt-get','install','-y','python-pip'], shell=True, stdin=None, stdout=None)

#installs python-dev, which is needed for various commands to work
Popen(['apt-get','install','-y','python-dev'], shell=True, stdin=None, stdout=None)

#installs Screen so we can connect to console on routers/switches
Popen(['apt-get','install','-y','screen'], shell=True, stdin=None, stdout=None)

#installs MOSH
Popen(['apt-get','install','-y','mosh'], shell=True, stdin=None, stdout=None)

#installs openswan for L2TP VPN connectivity
#Popen('apt-get install -y openswan', shell=True, stdin=None, stdout=None)

#installs sh via pip
Popen('pip install sh', shell=True, stdin=None, stdout=None)

#copies ipchange bash script
Popen('cp /home/pi/JumPi/scripts/ipchange /etc/dhcp/dhclient-exit-hooks.d', shell=True, stdin=None, stdout=None)

print "\nDon't forget to configure btsync!"
