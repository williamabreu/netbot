import threading
from netbot.keys import Keys
from netbot.mikrotik.Routerboard import Routerboard


class MikrotikWorker(threading.Thread):
    def __init__(self, target_hosts):
        super().__init__()
        self.__hosts = target_hosts

    def run(self):
        for ip in self.__hosts:
            try:
                rb = Routerboard(ip)
                rb.api_connect(Keys.username, Keys.password)
                print(ip, rb.get_identity(), rb.get_routerboard()['model'], sep=',')
                rb.api_disconnect()
            except ConnectionError as e:
                print(ip, 'ERROR', e, sep=',')
