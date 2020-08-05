# import librouteros
# import telnetlib
# import paramiko
import json
from netbot.mikrotik.Worker import MikrotikWorker
from netbot.zabbix.Zabbix import Zabbix
from netbot.proc.OutputHandler import OutputHandler


# Number of threads:
N_THREADS = 4


# Thread load balance:
def balance(length):
    slices = []
    last = 0
    num_elements = length
    num_threads = N_THREADS
    for i in range(N_THREADS):
        part_size = round(num_elements / (num_threads - i))
        slices.append(slice(last, last + part_size))
        num_elements -= part_size
        last += part_size
    return slices


def main():
    zabbix_hosts = None
    
    with open('zabbix_hosts.json') as fp:
        zabbix_hosts = json.load(fp)
    
    hosts = [host['ip'] for host in zabbix_hosts]
    slices = balance(len(hosts))
    threads = []
    # print(len(slices))
    
    for interval in slices:
        worker = MikrotikWorker(hosts[interval])
        worker.start()
        threads.append(worker)
    
    for thread in threads:
        thread.join()
    
    output = OutputHandler.get_instance()
    output.save()
    

if __name__ == '__main__':
    main()
