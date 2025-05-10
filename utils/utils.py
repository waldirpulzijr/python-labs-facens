from configurations.configurations import Configurations
from datetime import date

class Utils():
    def __init__(self):
        self.__configurations = Configurations()

    def read_file(self):
        with open(self.__configurations, 'r') as file:
            return list(map(lambda x: x.replace('\n', ''), file.readlines()))

    def wrote_file(self):
        with open(self.__configurations, 'a') as file:
            file.write(f'{str(date.today())} - {_type} - R$ {value} - {description}')
