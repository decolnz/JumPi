JumPi
=====

Turning a Raspberry Pi into a remote access network config jumphost.

The goal is to provide a small tool that can be plugged into equipment in a rack and then remotely accessed to complete upgrades, change configs, etc.

Installation
=====

To install without GitHub credentials:

	wget https://github.com/bronwynlewis/JumPi/archive/master.zip
	unzip master.zip
	rm master.zip
	mv JumPi-master/ JumPi/

To install necessary packages and move files:

	sudo python /home/pi/JumPi/install.py

To install BTsync, including basic config and run at boot:

	sudo python /home/pi/JumPi/btsync_install.py

For details on the BTsync installation and for Wifi configuration, see NOTES.

If you're using a brand new Pi, you will want to patch against Shellshock:

	sudo apt-get update && sudo apt-get -y dist-upgrade

This tests for Shellshock:

	env X="() { :;} ; echo busted" `which bash` -c "echo completed"
