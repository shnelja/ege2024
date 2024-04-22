from ipaddress import *

ip = '105.224.200.224'
mask = '255.255.255.224'

count = 0
net = ip_network(f'{ip}/{mask}', False)
for host in list(net.hosts()):
    if bin(int(host))[2:].zfill(32).count('1') % 4 == 0:
        count += 1
print(count)
