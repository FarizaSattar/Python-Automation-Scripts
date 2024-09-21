import os

def ping_test(hosts):
    for host in hosts:
        response = os.system(f'ping -c 1 {host}')
        if response == 0:
            print(f'{host} is reachable')
        else:
            print(f'{host} is not reachable')

hosts = ['8.8.8.8', 'www.google.com', '192.168.1.1']
ping_test(hosts)
