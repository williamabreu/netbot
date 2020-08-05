import threading
from netbot.keys import Keys
from netbot.mikrotik.Routerboard import Routerboard
from netbot.proc.OutputHandler import OutputHandler


class MikrotikWorker(threading.Thread):
    def __init__(self, target_hosts):
        super().__init__()
        self.__hosts = target_hosts
        self.__output = OutputHandler.get_instance()

    def run(self):
        for ip in self.__hosts:
            try:
                rb = Routerboard(ip)
                rb.api_connect(Keys.username, Keys.password)
                self.__output.register(ip, rb.get_identity(), rb.get_routerboard()['model'])
                rb.api_disconnect()
            except ConnectionError as e:
                self.__output.register(ip, 'ERROR', e)
