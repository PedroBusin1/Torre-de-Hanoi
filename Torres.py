from Disco import *
from Pino import *


class Torres:
    """
       Classe que controla os 3 pinos do jogo de Torre de Hanoi

    """
    __atributos = {'tamanho'}
    __metodos = {'__init__', '__str__', 'getTamanho', 'getManual', 'getAtributos', 'getMetodos'}

    def __init__(self, pino1, pino2 = Pino([]), pino3 = Pino([])):
        """
           Metodo construtor, recebe os
        """
        self.pino1 = pino1
        self.pino2 = pino2
        self.pino3 = pino3

    def __str__(self):
        """
           Metodo que retorna uma representação visual do jogo em str

           (Torres) -> str
        """
        return None

    def move_disco(self,pino_que_retira,pino_que_recebe):
        """
           Recebe dois dos pinos do jogo, verifica se o disco do topo do primeiro pino é maior que disco do topo
           do segundo disco ou se não há disco , caso sim, move o disco do topo do pino 1 para o pino 2, caso não
           retorna False

           (Pino,Pino) -> Sem retorno(atualiza Torres) ou False
        """
        return None

    def tamanho_pinos(self):
        """
           Retorna uma tupla com o tamanho o número de discos em cada pino

           (Torres) -> tuple(int, int, int)
        """
        return None

    def getAtributos():
        """
            Esta função estática (chamada sempre através de Tela.getAtributos()) retorna um
            conjunto com os nomes dos atributos desta classe.

            (None) -> set
        """
        return __atributos

    def getMetodos():
        """
            Esta função estática (chamada sempre através de Tela.getMetodos()) retorna um
            conjunto com os nomes dos métodos desta classe.

            (None) -> set
        """
        return __metodos

    def getManual():
        """
            Esta função estática (chamada sempre através de Tela.getManual()) retorna um
            dicionário que mapeia os nomes dos atributos e métodos às suas descrições.

            (None) -> dict
        """
        manual = dict()
        manual['__init__']                = Torres.__init__.__doc__
        manual['__str__']                 = Torres.__str__.__doc__
        manual['move_disco']              = Torres.move_disco.__doc__
        manual['tamanho_pinos']           = Torres.tamanho_pinos.__doc__
        manual['getManual']               = Torres.getManual.__doc__
        manual['getAtributos']            = Torres.getAtributos.__doc__
        manual['getMetodos']              = Torres.getMetodos.__doc__
        manual['pino1']                   ='# Primeiro pino do jogo'
        manual['pino2']                   ='# Segundo pino do jogo'
        manual['pino3']                   ='# Terceiro pino do jogo'
        return manual
