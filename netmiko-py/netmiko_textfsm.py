# Learning Python 2018 / Week 6, Netmiko Intro and Basics
from netmiko import Netmiko

my_device = {
    'host': '192.168.250.254',
    'username': 'user',
    'password': 'password',
    'secret': 'password',
    'device_type': 'cisco_ios'
}

net_conn = Netmiko(**my_device)
#output = net_conn.find_prompt()
net_conn.enable()
output = net_conn.send_command("show ip arp", use_textfsm=True)
print(output)
