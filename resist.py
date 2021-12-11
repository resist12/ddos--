import time
import os
import urllib.request
from platform import system
import socket
print("hello how are you w3 are RR and Resist societies this script is made by us we are hackers we are human----------")
time.sleep(0.25)
ip = socket.gethostname()
l = system()
print(f'lets begin {ip}')
print('------------------------------------------------------------------------------------------------------------------')
print('-------------------------------------------are u sure to use our tool---------------------')
print('------------------------------------------------------------------------------------------------------------------')
y = input('Y or N\n>')
if y == 'Y' and l == 'Linux':
    site = input('site name here >')
    if site.startswith('http://'):
        site = site
    else:
        site1 = 'http://' + site
    try:
        urllib.request.urlopen(site1)
        print(f'found this {site1}')
    except:
        print('found nothing')
    print("page will be clear at 10s")
    time.sleep(10)
    os.system('clear')
    print('Wait')
    time.sleep(5)
    os.system(f'ping {site} -t 100')
