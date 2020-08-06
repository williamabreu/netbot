from datetime import datetime


class OutputHandler:
    __INSTANCE = None

    def __init__(self):
        self.__cached_data = []

    @staticmethod
    def get_instance():
        if OutputHandler.__INSTANCE is None:
            OutputHandler.__INSTANCE = OutputHandler()
        return OutputHandler.__INSTANCE
    
    def register(self, *args):
        self.__cached_data.append(','.join(map(str, args)))

    def save(self):
        filename = datetime.now().isoformat().replace(':', '') + '.csv'
        with open(filename, 'w') as fp:
            # fp.write('IP,IDENTITY,MODEL\n')
            for line in self.__cached_data:
                fp.write(line + '\n')
                