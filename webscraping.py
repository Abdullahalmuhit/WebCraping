import requests
import socket
import dns.resolver
import tldextract
import urllib.request
# for internal pc information
import getpass
import os.path
import os
import re
import json
from urllib.request import urlopen 

url = input("Enter Your URL: ")
info = tldextract.extract(url)

def get_status():
    response = requests.get('https://'+url)
    status = response.status_code
    if status == 200:
        print("Website Exist")
    else:
        print("There is a problem on your website")

def dnfresolver():
    answers = dns.resolver.query(url,'NS')
    for server in answers:
        print (server)
    

def get_ip_servername():
    IP = socket.gethostbyname(url)
    try:
        addr = socket.gethostbyaddr(IP)
        print("Addr  Is:",addr ) 
    except Exception as e:
        print(str(e))
    
    print("IP  Is:",IP )


#regional details
def regional_details():
    urls = 'http://ipinfo.io/json'
    response = urlopen(urls)
    data = json.load(response)
    IP=data['ip']
    org=data['org']
    city = data['city']
    country=data['country']
    region=data['region']
    print('Your IP detail\n ')
    print('IP : {4} \nRegion : {1} \nCountry : {2} \nCity : {3} \nOrg : {0}'.format(org,region,country,city,IP))  


get_status()
dnfresolver()
get_ip_servername()

# print(socket.gethostbyname('cleopatra.io'))
# print(socket.gethostbyaddr('63.245.208.212'))
requests.get('https://'+url)

#get domain sub domaine
print("Domain Name: ", info.domain)
print("Subdomain: ", info.subdomain)
print("Suffix: ", info.suffix)
print("Domain with suffix: ", info.registered_domain)
print("Full Domain: ", '.'.join(info))

# for internal pc information
# username = getpass.getuser()
# print(username)
# homedir = os.path.expanduser("~")
# print(homedir)
regional_details()






