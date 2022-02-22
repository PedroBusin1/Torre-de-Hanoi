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



from Ferramentas import *
from Tela import *
from Torres import *
from Pino import *
from InterfaceUsuario import *
from Exceções import *
from Arquivos import *

class TorreDeHanoi(Ferramentas):
    """
        Classe que contrala a funcionalidade do jogo. Conectando todas as classes relacionadas a mecânica dp jogo.
    """

    def __init__(self, nDiscos = 3):
        """
            Método construtor que cria uma nova partida com as configuraçãoes passadas:
            - Quantidade de discos no jogo (padrão 3)

        """
        pass


    def verifica_termino(self):
        """
            Verifica se o jogo terminou.
        """
        pass


    def recebe_jogada(self):

        """ Recebe do jogador de qual pino ele quer retirar um disco e de qual ele quer colocar o disco retirado;
        retorna uma tupla com o valor inteiro dos números escolhidos, caso válidos.

        (TorreDeHanoi) -> tuple

        """

        pino_saida = input('Informe o número do pino o qual o jogador deseja retirar o disco: ')
        pino_recebe = input('Informe o número do pino o qual o jogador deseja colocar o disco: ')
        try:
            verifica_pinos(pino_saida,pino_recebe)
            pino_saida = int(pino_saida)
            pino_recebe = int(pino_recebe)
            return (pino_saida, pino_recebe)

        except CommandError:
            print('Ocorreu um erro na escolha dos pinos, devem ser fornecidos dois valores diferentes entre'
                  '1 e 3!!')
            erro = 'Erro: o Usuario informou um valor inadequado para o pino de saida e de entrada, '
            msg = 'Ocorreu um erro na escolha dos pinos, devem ser fornecidos dois valores diferentes entre 1 e 3!!, '
            trat = 'Tratamento do erro: Volta ao começo do loop de jogo e ignora a jogada incorreta.'
            Arquivos.registraLog(erro + msg + trat)



    def jogada(self):
        """
            Realiza a jogada.
        """
        pass




    def __str__(self):
        """
            Metodo que cria uma representação em string da descrição das classes, seus métodos e atributos
        """
        saida = ""

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

        saida += 'MANUAL DA CLASSE EXCEÇOES\n'

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
        manualTorreDeHanoi['recebe_jogada']      = TorreDeHanoi.recebe_jogada.__doc__
        manualTorreDeHanoi['jogada']             = TorreDeHanoi.jogada.__doc__
        manualTorreDeHanoi['verifica_termino']   = TorreDeHanoi.verifica_termino.__doc__
        manualTorreDeHanoi['nDiscos']            = 'Determina o número de discos do jogo'
        manualTorreDeHanoi['ComTempo']           = 'Determina se o jogo tera ou não liminte de tempo'
        manualTorreDeHanoi['LimJogadas']         = 'Determina se o jogo tera ou não liminte de jogadas'

        saida += 'MANUAL DA CLASSE TORREDEHANOI\n'

        for chave in manualTorreDeHanoi:
            saida += f'{chave} : {manualTorreDeHanoi[chave]}\n'
        saida += '\n'

        return saida




while True:

    Tela.limpa_tela()

    opcao_escolhida = Tela.menuPrincipal()

    Tela.limpa_tela()
    if opcao_escolhida == '4':
        print(TorreDeHanoi())
        input('== Aperte enter para retornar ao menu principal ==')

    if opcao_escolhida == '5':

        Tela.limpa_tela()

        Tela.TelaEstats()

    if opcao_escolhida in ('1','2','3'):

        Tela.limpa_tela()

        print('\n ========= Em desenvolvimento ==========\n')
        input('== Aperte enter para retornar ao menu principal ==')
