import librouteros
import json


class Routerboard:
    def __init__(self, host):
        self.__host = host
        self.__api = None

    def api_connect(self, username, password, port=8728):
        try:
            # version >= 6.43
            self.__api = librouteros.connect(
                host=self.__host,
                username=username,
                password=password,
                login_method=librouteros.plain
            )
        except:
            try:
                # version < 6.43
                self.__api = librouteros.connect(
                    host=self.__host,
                    username=username,
                    password=password,
                    login_method=librouteros.token
                )
            except:
                raise ConnectionError('Connection error')
                # raise ConnectionError('Check if the API is enabled in the router')
                # raise ConnectionError('Check if the firewall or ACL is blocking the connection')

    def api_disconnect(self):
        self.__api.close()

    def get_identity(self):
        path = self.__api.path('system', 'identity')
        identity = tuple(path)[0]['name']
        return identity
    
    def get_routerboard(self):
        path = self.__api.path('system', 'routerboard')
        rb = tuple(path)[0]
        return rb
