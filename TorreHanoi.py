"""
   Este program consiste no jogo Torre de Hanoi.
   "Torre de Hanói é um quebra-cabeça que consiste em uma base contendo três pinos, em um dos quais são
   dispostos alguns discos uns sobre os outros, em ordem crescente de diâmetro, de cima para baixo.
   O problema consiste em passar todos os discos de um pino para outro qualquer, usando um dos pinos como
   auxiliar, de maneira que um disco maior nunca fique em cima de outro menor em nenhuma situação.
   O número de discos pode variar sendo que o mais simples contém apenas três."
   - Fonte: https://pt.wikipedia.org/wiki/Torre_de_Han%C3%B3i
   Opções de costomização:
   - Quantidade de discos (padrão 3)
   - Com tempo ou sem tempo (padrão sem tempo)
   - Com ou sem limite de jogadas (padrão sem limite)
   O jogo será formado por uma base contendo 3 PINOS e o número de DISCOS escolhidos, representada como:
               |                          |                     |
               |                          |                     |
              □□□                         |                     |
             □□□□□                        |                     |
            □□□□□□□                       |                     |
   O jogador poderá realizar sucessivas jogadas, que consintem em mover o Disco do topo de um Pino para outro,
   até que o jogo se encerre.
"""

# Document properties
__author__ = ['Pedro_Henrique_Busin_Cambruzzi', 'Pedro_Henrique_de_Miranda_Pinto']
__copyright__ = 'Copyright_2022'
__credits__ = __author__
__license__ = 'GPL'
__version__ = '1.0.0'
__maintainer__ = 'Pedro Henrique Busin Cambruzzi'
__email__ = 'pedrobusin@poli.ufrj.br'
__status__ = 'Production'

from InterfaceUsuario import *
from Ferramentas import *
from Tela import *
from Torres import *
from Pino import *
from Disco import *


class TorreDeHanoi(Ferramentas):
    """
        Classe que contrala a funcionalidade do jogo. Conectando todas as classes relacionadas a mecânica dp jogo.
    """

    def __init__(self, nDiscos = 3, ComTempo = False, LimJogadas = False):
        """
            Método construtor que cria uma nova partida com as configuraçãoes passadas:
            - Quantidade de discos no jogo (padrão 3)
            - Jogo com ou sem limite de tempo (padrão sem)
            - Jogo com ou sem limite de jogadas (padrão sem)
        """
        pass

    def __str__(self):
        """
            Metodo que cria uma representação em string da descrição das classes, seus métodos e atributos
        """
        saida = ""

        manualDisco = Disco.getManual()

        saida += 'MANUAL DA CLASSE DISCO\n'

        for chave in manualDisco:
            saida += f'{chave} : {manualDisco[chave]}\n'
        saida +='\n'

        manualPino = Pino.getManual()

        saida += 'MANUAL DA CLASSE PINO\n'

        for chave in manualPino:
            saida += f'{chave} : {manualPino[chave]}\n'
        saida +='\n'

        saida += 'MANUAL DA CLASSE TORRES\n'

        manualTorres = Torres.getManual()

        for chave in manualTorres:
            saida += f'{chave} : {manualTorres[chave]}\n'
        saida +='\n'

        saida += 'MANUAL DA CLASSE FERRAMENTAS\n'

        manualFerramentas = Ferramentas.getManual()

        for chave in manualFerramentas:
            saida += f'{chave} : {manualFerramentas[chave]}\n'
        saida +='\n'

        manualInterfaceUsuario = InterfaceUsuario.getManual()

        saida += 'MANUAL DA CLASSE INTERFACE USUARIO\n'

        for chave in manualInterfaceUsuario:
            saida += f'{chave} : {manualInterfaceUsuario[chave]}\n'
        saida +='\n'

        manualTela = Tela.getManual()

        saida += 'MANUAL DA CLASSE TELA\n'

        for chave in manualTela:
            saida += f'{chave} : {manualTela[chave]}\n'
        saida +='\n'      

        return saida

    def jogada(self):
        """
            Realiza a jogada.
        """
        pass

    def verifica_termino(self):
        """
            Verifica se o jogo terminou.
        """
        pass
    
while True:
    if Tela.menuPrincipal():
        print(TorreDeHanoi())



