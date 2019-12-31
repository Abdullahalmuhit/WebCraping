import requests
import socket
url = input("Enter Your URL: ")
response = requests.get('https://'+url)
status = response.status_code
IP = socket.gethostbyname(url)
addr = socket.gethostbyaddr(IP)
if status == 200:
    print("Website Exist")
else:
    print("There is a problem on your website")

print("IP  Is:",IP )
print("Addr  Is:",addr )
