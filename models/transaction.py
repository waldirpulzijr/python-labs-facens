from utils.utils import Utils

class Transaction():
    def __init__(self, type=None, value=None, description=None):
        self.__type = type
        self.__value = value
        self.__description = description

        self.__utils = Utils()

    def save(self):
        self.__utils.wrote_file(
            self.__type, self.__value, self.__description    
        )
   
    def view(self):
        for t in self.__utils.read_file():
            print(f'')
                