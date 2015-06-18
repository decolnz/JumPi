import sys
import re
import urllib2
from sh import ifconfig
from subprocess import Popen, PIPE

# this removes the ifconfig file if present, prior to running
Popen('rm /home/pi/JumPi/cruft/ifconfig_*', shell=True, stdin=PIPE).communicate("y")

# this removes the IP file if present, prior to running
Popen('rm /home/pi/JumPi/jump_ip.txt', shell=True, stdin=PIPE).communicate("y")

# this uses sh, which allows you to interface with the subprocess ifconfig
myEth0 = ifconfig("eth0")
myWlan0 = ifconfig("wlan0")

# this will be for the VPN IP
#myIPvpn = ifconfig("")

# this just saves the raw ifconfig output for specified interface to txt
file_ifconfig = open("/home/pi/JumPi/cruft/ifconfig_eth0.txt", "w")
file_ifconfig.writelines(myEth0)
file_ifconfig.close()

file_ifconfig = open("/home/pi/JumPi/cruft/ifconfig_wlan0.txt", "w")
file_ifconfig.writelines(myWlan0)
file_ifconfig.close()

# this will be for the VPN IP
#file_ifconfig = open("/home/pi/JumPi/cruft/ifconfig_vpn.txt", "w")
#file_ifconfig.writelines(myIPvpn)
#file_ifconfig.close()

# this opens the ifconfig output + allows you to interact with it as a string
with open ("/home/pi/JumPi/cruft/ifconfig_eth0.txt", "r") as myfile:
    data=myfile.read().replace('\n', '')

with open ("/home/pi/JumPi/cruft/ifconfig_wlan0.txt", "r") as myfile:
    data=myfile.read().replace('\n', '')

# this checks what your public IP is
def publicIP(myEth0):
    ip_checker_url = "http://checkip.dyndns.org/"
    address_regexp = re.compile ('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
    response = urllib2.urlopen(ip_checker_url).read()
    result = address_regexp.search(response)
    if result:
            return result.group()
    else:
            return None

# this grabs your "private" IP from the raw ifconfig
def privateEth0(myEth0):
    address_regexp = re.compile ('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
    response = data
    result = address_regexp.search(response)
    if result:
            return result.group()
    else:
            return None

def privateWlan0(myWlan0):
    address_regexp = re.compile ('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
    response = data
    result = address_regexp.search(response)
    if result:
            return result.group()
    else:
            return None

# this writes your public and private IP to a text file
file_ip = open("/home/pi/JumPi/sync/jump_ip.txt", "w")
file_ip.writelines("My public IP is: " + publicIP(myEth0) + "\n")
file_ip.writelines("My private eth0 IP is: " + privateEth0(myEth0) + "\n")
file_ip.writelines("My private wlan0 IP is: " + privateWlan0(myWlan0))
file_ip.close()
