from subprocess import Popen, PIPE

#creates folder, downloads, unpacks btsync, copies over config file
Popen('mkdir /home/pi/.btsync', shell=True, stdin=None, stdout=None).wait()
Popen('wget -O /home/pi/.btsync/stable http://download-new.utorrent.com/endpoint/btsync/os/linux-arm/track/stable', shell=True, stdin=None, stdout=None).wait()
Popen('tar -xvf /home/pi/.btsync/stable -C /home/pi/.btsync', shell=True, stdin=None, stdout=None).wait()

#the section below seems to be failing right now in this script

Popen('cp /home/pi/JumPi/scripts/btsync.config /home/pi/.btsync/', shell=True, stdin=None, stdout=None).wait()

#copies btsync auto start on boot, creates start/stop shortcut, starts btsync
Popen('cp /home/pi/JumPi/scripts/btsync /etc/init.d/', shell=True, stdin=None, stdout=None).wait()
Popen('chmod 755 /etc/init.d/btsync', shell=True, stdin=None, stdout=None).wait()

Popen('/etc/init.d/btsync start', shell=True, stdin=None, stdout=None).wait()

print "\nDon't forget to edit the btsync.config file and set-up your sync folder through a browser on the same LAN:\n\nhttp://m.y.I.P:8888/gui/"
