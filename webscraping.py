import requests
import socket
import dns.resolver
import tldextract




url = input("Enter Your URL: ")
info = tldextract.extract(url)

answers = dns.resolver.query(url,'NS')

response = requests.get('https://'+url)
status = response.status_code
IP = socket.gethostbyname(url)
if IP is not None:
    addr = socket.gethostbyaddr(IP)
else:
    print('null')

if status == 200:
    print("Website Exist")
else:
    print("There is a problem on your website")
# print(socket.gethostbyname('cleopatra.io'))
# print(socket.gethostbyaddr('63.245.208.212'))
requests.get('https://'+url)

#to get ip address
print("IP  Is:",IP )
#to get domain address
print("Addr  Is:",addr )
#to get name server
for server in answers:
    print (server)

#get domain sub domaine

print("Details:" , info)
print("Domain Name: ", info.domain)
print("Subdomain: ", info.subdomain)
print("Suffix: ", info.suffix)
print("Domain with suffix: ", info.registered_domain)
print("Full Domain: ", '.'.join(info))


