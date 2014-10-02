from subprocess import Popen, PIPE

#installs PIP, which is needed to install sh for myIP.py
Popen('apt-get install -y python-pip', shell=True, stdin=PIPE)

#installs python-dev, which is needed for various commands to work
Popen('apt-get install -y python-dev', shell=True, stdin=PIPE)

#installs Screen so we can connect to console on routers/switches
Popen('apt-get install -y screen', shell=True, stdin=PIPE)

#installs openswan for L2TP VPN connectivity
Popen('apt-get install -y openswan', shell=True, stdin=PIPE)

print "\nDon't forget to install sh via pip and configure btsync!"
