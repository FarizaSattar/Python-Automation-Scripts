import paramiko

def test_ssh_connection(host, username, password):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh.connect(host, username=username, password=password)
        print(f'Successful SSH connection to {host}')
    except Exception as e:
        print(f'Failed to connect to {host}: {e}')
    finally:
        ssh.close()

servers = [
    {'host': '192.168.1.10', 'username': 'admin', 'password': 'password'},
    {'host': '192.168.1.11', 'username': 'admin', 'password': 'password'}
]

for server in servers:
    test_ssh_connection(server['host'], server['username'], server['password'])
