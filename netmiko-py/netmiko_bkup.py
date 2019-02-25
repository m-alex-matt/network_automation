# Learning Python 2018 / Week 6, Netmiko Intro and Basics
from netmiko import Netmiko
import datetime

CUR_TIME = str(datetime.datetime.today().isoformat()[:-7])
CUR_DIR = '/home/michael/Desktop/config/base_config'

def backup(net_conn, hostn):
    net_conn.enable()
    command = "show running-config"
    output = net_conn.send_command(command)
    try:
        with open(f'{CUR_DIR}/{hostn}/{hostn}.config', mode='x') as f:
            f.write(output)
    except FileExistsError:
        with open(f'{CUR_DIR}/{hostn}/{hostn}.config', mode='r') as f:
            with open(f'{CUR_DIR}/{hostn}/{hostn}.config_{CUR_TIME}', mode='w') as f_old:
                f_old.write(f.read())
        with open(f'{CUR_DIR}/{hostn}/{hostn}.config', mode='w') as f:
            f.write(output)

def main():
    my_device = {
        'host': '',
        'username': 'user',
        'password': 'password',
        'secret': 'password',
        'device_type': 'cisco_ios'
    }   

    my_device['host'] = input("What is the IP address of your device? ")
    host_name = input("What is the hostname of your device? ")
    net_conn = Netmiko(**my_device)

    backup(net_conn, host_name)

if __name__ == '__main__':
    main()
