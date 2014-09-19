# for using .write and .writelines
import sys
# for using ifconfig to pull interface data
from sh import ifconfig

# creates/opens specified file
file = open("/jump1_ip.txt", "w")

# defines variable name for ifconfig output
myIP = ifconfig("en0")

# writes ifconfig output to specified file
file.writelines(myIP)

# closes file to free up processes
file.close()

'' Need to still 1) grab only the ip address, 2) either check IP at regular intervals or whenever the computer connects and gets dhcp, 3) make sure it starts on boot-up ''
