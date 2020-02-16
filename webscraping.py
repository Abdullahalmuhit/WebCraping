import requests
import socket
import dns.resolver
import tldextract
import urllib.request
# for internal pc information
import getpass
import os.path
import os

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
username = getpass.getuser()
print(username)
homedir = os.path.expanduser("~")
print(homedir)




