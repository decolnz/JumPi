import sys
import re
import urllib2
from sh import ifconfig

myIP = ifconfig("en0")

file_ifconfig = open("jump1_ifconfig.txt", "w")
file_ifconfig.writelines(myIP)
file_ifconfig.close()

with open ("jump1_ifconfig.txt", "r") as myfile:
    data=myfile.read().replace('\n', '')

def publicIP(myIP):
    ip_checker_url = "http://checkip.dyndns.org/"
    address_regexp = re.compile ('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
    response = urllib2.urlopen(ip_checker_url).read()
    result = address_regexp.search(response)
    if result:
            return result.group()
    else:
            return None

def privateIP(myIP):
    address_regexp = re.compile ('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
    response = data
    result = address_regexp.search(response)
    if result:
    	    return result.group()
    else:
            return None

file_ip = open("jump1_ip.txt", "w")
file_ip.writelines("My public IP is: " + publicIP(myIP) + "\n")
file_ip.writelines("My private IP is: " + privateIP(myIP))
file_ip.close()
