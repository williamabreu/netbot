# import librouteros
# import telnetlib
# import paramiko
# import json
from netbot.mikrotik.Worker import MikrotikWorker


def main():
    hosts = [
        # '192.168.56.45',
        # '192.168.56.42',
        # '192.168.56.34',
        '172.16.240.1',
        '177.93.103.102',
        '172.16.240.4',
    ]

    worker1 = MikrotikWorker(hosts)
    worker1.start()


    # SSH
    # ssh = paramiko.SSHClient()
    # ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    # ssh.connect(hostname='192.168.56.30', username='admin', password='')
    

if __name__ == '__main__':
    main()
