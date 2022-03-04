"""
   Este programa consiste no jogo Torre de Hanoi.

   "Torre de Hanói é um quebra-cabeça que consiste em uma base contendo três torres, em um dos quais são
   dispostos alguns discos uns sobre os outros, em ordem crescente de diâmetro, de cima para baixo.

   O problema consiste em passar todos os discos de uma torre para outra qualquer, usando uma das torres como
   auxiliar, de maneira que um disco maior nunca fique em cima de outro menor em nenhuma situação.

   O número de discos pode variar sendo que o mais simples contém apenas três."

   - Fonte: https://pt.wikipedia.org/wiki/Torre_de_Han%C3%B3i

   Opções de customização:

   - Quantidade de discos

   O jogo será formado por uma base contendo 3 TORRES e o número de DISCOS escolhidos, representada como:

               |                          |                     |
               |                          |                     |
              □□□                         |                     |
             □□□□□                        |                     |
            □□□□□□□                       |                     |

   O jogador poderá realizar sucessivas jogadas, que consintem em mover o Disco do topo de uma Torre para outra,
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

from TelaHanoi import *
from Exceções import *
from Arquivos import *
import time

class TorreDeHanoi:
    """
        Classe que controla a funcionalidade do jogo. Conectando todas as classes relacionadas a mecânica do jogo.
    """
    __metodos = {'interacao', 'verifica_termino', '__str__','getAtributos','getMetodos','getManual'}
    __atributos = {}

    def interacao(self, torre, informacao_movimento):
        if len(informacao_movimento) == 0:
            informacao_movimento.append(torre)
            self.informacoes['text'] = 'Escolha a torre para a qual deseja mover:'
            self.informacoes.place(x=90,y=45)
            self.torre_1['command'] = lambda: TorreDeHanoi.interacao(self, 0, [torre])
            self.torre_2['command'] = lambda: TorreDeHanoi.interacao(self, 1, [torre])
            self.torre_3['command'] = lambda: TorreDeHanoi.interacao(self, 2, [torre])
        elif len(informacao_movimento) == 1:
            informacao_movimento.append(torre)
            movimentos = {0: 'Torre 1', 1: 'Torre 2', 2: 'Torre 3'}
            try:
                Erros.verifica_jogada(self.estado_torre[informacao_movimento[0]],self.estado_torre[informacao_movimento[1]])
                self.realiza_movimento_grafico(min(self.estado_torre[informacao_movimento[0]]),informacao_movimento[0],informacao_movimento[1])
                Arquivos.atualizaMovimentos(str(movimentos[informacao_movimento[0]])+'-'+str(movimentos[informacao_movimento[1]]), str(time.time() - self.inicio), self.estado_torre)
                self.inicio = time.time()
            except:
                messagebox.showinfo(message='Lance inválido, tente novamente!')
                erro = 'Erro: o Usuario informou um valor inadequado para o pino de saida e de entrada, '
                msg = 'Mensagem: Lance inválido, tente novamente!'
                trat = 'Tratamento do erro: Pede para o jogador fazer outra jogada.'
                Arquivos.registraLog(erro +' '+msg +' '+trat)
            self.informacoes['text'] = 'Escolha uma torre:'
            self.informacoes.place(x=170,y=45)
            self.torre_1['command'] = lambda: TorreDeHanoi.interacao(self, 0, [])
            self.torre_2['command'] = lambda: TorreDeHanoi.interacao(self, 1, [])
            self.torre_3['command'] = lambda: TorreDeHanoi.interacao(self, 2, [])
            if TorreDeHanoi.verifica_termino(self):
                messagebox.showinfo(message='Parabéns, você venceu!!')
                self.menu_principal()

    def verifica_termino(partida):
        """
           Verifica se o jogo terminou.
        """
        if (len(partida.estado_torre[0]) == 0 and len(partida.estado_torre[1]) == 0) or (len(partida.estado_torre[0]) == 0 and len(partida.estado_torre[2]) == 0):
            Arquivos.altera_status_partida()
            Estatisticas.atualizaEstatisticas()
            return True
        else:
            return False
    
    def getAtributos():
        """
            Esta função estática (chamada sempre através de TorreDeHanoi.getAtributos()) retorna um
            conjunto com os nomes dos atributos desta classe.

            (None) -> set
        """
        return __atributos

    def getMetodos():
        """
            Esta função estática (chamada sempre através de TorreDeHanoi.getMetodos()) retorna um
            conjunto com os nomes dos métodos desta classe.

            (None) -> set
        """
        return __metodos

    def getManual():
        """
            Esta função estática (chamada sempre através de TorreDeHanoi.getManual()) retorna um
            dicionário que mapeia os nomes dos atributos e métodos às suas descrições.
            (None) -> dict
        """

    def __str__(self):
        """
            Metodo que cria uma representação em string da descrição das classes, seus métodos e atributos
        """
        saida = ""

        manualTela = Tela.getManual()

        saida += 'MANUAL DA CLASSE TELA\n'

        for chave in manualTela:
            saida += f'{chave} : {manualTela[chave]}\n'
        saida +='\n'

        manualErros = Erros.getManual()
        saida += 'MANUAL DA CLASSE ERROS\n'

        for chave in manual_excecoes:
            saida += f'{chave} : {manual_excecoes[chave]}\n'
        saida += '\n'

        manualArquivos = Arquivos.getManual()

        saida += 'MANUAL DA CLASSE ARQUIVOS\n'

        for chave in manualArquivos:
            saida += f'{chave} : {manualArquivos[chave]}\n'
        saida += '\n'

        manualEstatisticas = Estatisticas.getManual()

        saida += 'MANUAL DA CLASSE ESTATISTICAS\n'

        for chave in manualEstatisticas:
            saida += f'{chave} : {manualEstatisticas[chave]}\n'
        saida += '\n'

        manualTorreDeHanoi = dict()
        manualTorreDeHanoi['TorreDeHanoi']       = TorreDeHanoi.__doc__
        manualTorreDeHanoi['__init__']           = TorreDeHanoi.__init__.__doc__
        manualTorreDeHanoi['__str__']            = TorreDeHanoi.__str__.__doc__
        manualTorreDeHanoi['getAtributos']       = TorreDeHanoi.getAtributos.__doc__
        manualTorreDeHanoi['getMetodos']         = TorreDeHanoi.getMetodos.__doc__
        manualTorreDeHanoi['interacao']          = TorreDeHanoi.interacao.__doc__
        manualTorreDeHanoi['getManual']         = TorreDeHanoi.getManual.__doc__
        manualTorreDeHanoi['verifica_termino']   = TorreDeHanoi.verifica_termino.__doc__

        saida += 'MANUAL DA CLASSE TORREDEHANOI\n'

        for chave in manualTorreDeHanoi:
            saida += f'{chave} : {manualTorreDeHanoi[chave]}\n'
        saida += '\n'

        return saida


