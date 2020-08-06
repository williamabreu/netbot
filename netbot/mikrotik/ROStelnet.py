from telnetlib import Telnet
import time


class ROStelnet:
    def  __init__(self):
        self.__telnet = None
    
    def connect(self, host, username, password, port=23):
        self.__telnet = Telnet(host, port)
        self.__telnet.read_until(b'Login: ')
        self.__telnet.write(username.encode('utf-8') + b'\r\n')
        self.__telnet.read_until(b'Password: ')
        self.__telnet.write(password.encode('utf-8') + b'\r\n')
        self.__telnet.read_until(b'> ')
        self.__wait_response()
        self.__read_buffer()
    
    def disconnect(self):
        if self.__telnet:
            self.__telnet.close()
    
    def is_connected(self):
        if self.__telnet:
            try:
                response = self.exec_cmd('/system routerboard print')
                return len(response) > 0
            except:
                return False
        else:
            return False

    def exec_cmd(self, cmd):
        self.__telnet.write(cmd.encode('utf-8') + b'\r\n')
        self.__wait_response()
        buffer = self.__read_buffer()
        return buffer
    
    def __read_buffer(self):
        buffer = self.__telnet.read_eager()
        concat = ''
        while buffer != b'':
            concat += buffer.decode('utf-8')
            buffer = self.__telnet.read_eager()
        return concat
    
    def __wait_response(self):
        time.sleep(0.5)

if __name__ == '__main__':

    x = ROStelnet()
    x.connect('192.168.93.1', 'admin', 'admin')
    
    try:
        while True:
            r = x.exec_cmd(input('input> '))
            print(r)
    except:
        x.disconnect()
    