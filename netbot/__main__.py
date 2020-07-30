# import librouteros
# import telnetlib
# import paramiko
# import json
from netbot.keys import Keys
from netbot.mikrotik.Routerboard import Routerboard


def main():
    hosts = [
        # '192.168.56.45',
        # '192.168.56.42',
        # '192.168.56.34',
        '172.16.240.49',
    ]

    for ip in hosts:
        rb = Routerboard(ip)
        rb.api_connect(Keys.username, Keys.password)
        print(ip, rb.get_identity(), rb.get_routerboard()['model'], sep=',')
        rb.api_disconnect()

    # SSH
    # ssh = paramiko.SSHClient()
    # ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    # ssh.connect(hostname='192.168.56.30', username='admin', password='')
    

if __name__ == '__main__':
    main()
