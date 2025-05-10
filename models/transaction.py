from utils.utils import Utils

### Teste

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
        for transaction in self.__utils.read_file():
            print(f'Operation: {transaction[0]} - Value: {transaction[1]} - Description: {transaction[2]}')
                