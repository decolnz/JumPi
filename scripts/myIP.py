import sys
import re
import urllib2
from sh import ifconfig

# this uses sh, which allows you to interface with the subprocess ifconfig
myIP = ifconfig("eth0")

# this just saves the raw ifconfig output for specified interface to txt
file_ifconfig = open("/home/pi/JumPi/cruft/jump_ifconfig.txt", "w")
file_ifconfig.writelines(myIP)
file_ifconfig.close()

# this opens the ifconfig output + allows you to interact with it as a string
with open ("/home/pi/JumPi/cruft/jump_ifconfig.txt", "r") as myfile:
    data=myfile.read().replace('\n', '')

# this checks what your public IP is
def publicIP(myIP):
    ip_checker_url = "http://checkip.dyndns.org/"
    address_regexp = re.compile ('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
    response = urllib2.urlopen(ip_checker_url).read()
    result = address_regexp.search(response)
    if result:
            return result.group()
    else:
            return None

# this grabs your "private" IP from the raw ifconfig
def privateIP(myIP):
    address_regexp = re.compile ('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
    response = data
    result = address_regexp.search(response)
    if result:
    	    return result.group()
    else:
            return None

# this writes your public and private IP to a text file
file_ip = open("/home/pi/JumPi/jump_ip.txt", "w")
file_ip.writelines("My public IP is: " + publicIP(myIP) + "\n")
file_ip.writelines("My private IP is: " + privateIP(myIP))
file_ip.close()
