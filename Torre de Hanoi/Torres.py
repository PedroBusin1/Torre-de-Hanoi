import Pino
from Exceções import *
from Arquivos import *


class Torres:
    """
       Classe que controla os 3 pinos do jogo de Torre de Hanoi.

    """
    __atributos = {'pino1', 'pino2', 'pino3'}
    __metodos = {'__init__', '__str__', 'getTamanho', 'getManual', 'getAtributos', 'getMetodos'}

    def __init__(self, pino1, pino2 =Pino, pino3 =Pino):
        """
           Metodo construtor, recebe os três pinos do jogo da Torre de Hanoi.
        """
        self.pino1 = pino1
        self.pino2 = pino2
        self.pino3 = pino3

    def __str__(self):
        """
           Metodo que retorna uma representação visual do jogo em str.

           (Torres) -> str
        """
        return None

    def move_disco(self,pino_saida,pino_recebe):
        """
           Recebe dois dos pinos do jogo, verifica se o disco do topo do primeiro pino é maior que disco do topo
           do segundo disco ou se não há disco , caso sim, move o disco do topo do pino 1 para o pino 2, caso não
           retorna False.

           (Pino,Pino) -> Sem retorno(atualiza Torres) ou False
        """
        try:
            verifica_discos(pino_saida.disco_topo(), pino_recebe.disco_topo())
            disco_movido = pino_saida.retira_disco()
            pino_recebe.coloca_disco(disco_movido)

        except CommandError:
            print('O jogador tentou colocar um disco maior em cima de um menor ou tentou retirar o disco de uma torre vazia, essa jogada é invalida!!')
            erro = 'Erro: o Usuario tentou colocar um disco maior em cima de um menor ou tentou retirar o disco de uma torre vazia, '
            msg = 'O jogador tentou colocar um disco maior em cima de um menor ou tentou retirar o disco de uma torre vazia, essa jogada é invalida!!'
            '1 e 3!!, '
            trat = 'Tratamento do erro: Volta ao começo do loop de jogo e ignora a jogada incorreta.'
            Arquivos.registraLog(errp + msg + trat)

        return None

    def tamanho_pinos(self):
        """
           Retorna uma tupla com o tamanho o número de discos em cada pino.

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
        manual['Torres']                  = Torres.__doc__
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
