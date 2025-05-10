from configuracoes.configurations import Configuracoes
from datetime import date

class Utils():
    def __init__(self):
        self.__configurations = Configuracoes()

    def read_file(self):
        with open(self.__configurations.file_output, 'r') as file:
            return list(map(lambda x: x.replace('\n', ''), file.readlines()))

    def wrote_file(self, _type, value, description):
        with open(self.__configurations.file_output, 'a') as file:
            file.write(f'{str(date.today())} - {_type} - R$ {value} - {description}')
