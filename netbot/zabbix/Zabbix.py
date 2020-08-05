from pyzabbix.api import ZabbixAPI


class Zabbix:
    def __init__(self, url):
        self.__url = url
        self.__api = None
    
    def api_connect(self, username, password):
        self.__api = ZabbixAPI(
            url=self.__url, 
            user=username,
            password=password
        )
    
    def api_disconnect(self):
        self.__api.user.logout()

    def get_monitored_hosts(self):
        monitored_hosts = self.__api.host.get(monitored_hosts=1, output='extend')
        return [
            {
                'hostid': host['hostid'],
                'hostname': host['host'],
                'ip': self.__api.hostinterface.get(hostids=host['hostid'])[0]['ip'],
            } 
            for host in monitored_hosts
        ]
