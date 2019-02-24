# Learning Python 2018 / Week 6, Netmiko Intro and Basics
from netmiko import Netmiko
from getpass import getpass

my_device = {
    'host': '192.168.250.254',
    'username': 'user',
    'password': getpass(),
    'secret': 'password',
    'device_type': 'cisco_ios'
}

net_conn = Netmiko(**my_device)
#output = net_conn.find_prompt()
net_conn.enable()
output = net_conn.send_command("show run")
print(output)
