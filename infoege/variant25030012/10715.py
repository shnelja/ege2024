from ipaddress import *

ip = '192.168.32.160'
mask = '255.255.255.240'

count = 0
net = ip_network(f'{ip}/{mask}')
for host in net:
    if bin(int(host))[2:].count('0') > 21:
        count += 1
print(count)
