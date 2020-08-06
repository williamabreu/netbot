import threading
from netbot.keys import Keys
from netbot.mikrotik.Routerboard import Routerboard
from netbot.proc.OutputHandler import OutputHandler
from netbot.mikrotik.ROStelnet import ROStelnet

from datetime import datetime

class MikrotikWorkerEnableAPI(threading.Thread):
    def __init__(self, target_hosts):
        super().__init__()
        self.__hosts = target_hosts
        self.__output = OutputHandler.get_instance()

    def run(self):
        for ip in self.__hosts:
            try:
                print(f'{datetime.now().isoformat()} :: Trying via telnet in {ip} ...')
                tn = ROStelnet()
                tn.connect(ip, Keys.username, Keys.password, 2300)
                while not tn.is_connected(): pass
                # tn.exec_cmd('/ip service set api address=177.66.48.0/28,177.66.48.214,177.93.103.190 port=8728')
                tn.exec_cmd('/ip service enable api')
                print(f'    -> Done via telnet - {ip}.')
            except: 
                print(f'    -> Error connecting via telnet - {ip}.')
