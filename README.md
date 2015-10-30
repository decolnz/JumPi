JumPi
=====

Turning a Raspberry Pi into a remote access network config jumphost.

The goal is to provide a small tool that can be plugged into equipment in a rack and then remotely accessed to complete upgrades, change configs, etc.

Alternately, you could use a dynamic DNS service to provide a hostname that you could remote access for your Raspberry Pi. But where's the fun in that? =)

Installation
=====

To install without GitHub credentials:

	wget https://github.com/bronwynlewis/JumPi/archive/master.zip
	unzip master.zip
	rm master.zip
	mv JumPi-master/ JumPi/

To install necessary packages and move files:

	sudo python /home/pi/JumPi/install.py

If you're using a brand new Pi:

	sudo apt-get update && sudo apt-get -y dist-upgrade

This assumes a public IP address is offered up via dhcp to the Raspberry Pi when it is deployed. This often is not the case, so in any instance when NAT dhcp is used, you would need to use an ssh tunnel, VPN, etc.

To sync the IP address written file to your local machine, you will also need a program such as syncthing, btsync, owncloud, or dropbox.


