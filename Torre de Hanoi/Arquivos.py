import os
import ast
from time import ctime


class Arquivos:
    """ Classe que contem todos os metodos que podem ser úteis na criação e atualização de arquivos. """

    __metodos = {'registraHistorico', 'atualizaMovimentos', 'atualizaDuracao', 'registraLog', 'getAtributos',
                 'getMetodos', 'getManual'}
    __atributos = {}

    def registraHistorico(nro_discos):

        ''' Esta função adiciona uma linha genérica a ultima linha do arquivo de histórico. '''

        arquivo_texto = open('historico.txt', 'a+')
        if os.stat(os.getcwd() + chr(92) + 'historico.txt').st_size == 0:
            arquivo_texto.write('[[], False,' + str(nro_discos) + ']')
            Arquivos.atualizaDuracao('0', True)
        else:
            arquivo_texto.write('\n' + '[[], False,' + str(nro_discos) + ']')
            Arquivos.atualizaDuracao('0', True)
        arquivo_texto.close()

    def atualizaDuracao(tempo_decorrido, nova_partida=False):

        ''' Esta função atualiza o arquivo com a duração das partidas até o último movimento feito. '''

        if nova_partida:
            arquivo_texto = open('duracao.txt', 'a+')
            if os.stat(os.getcwd() + chr(92) + 'duracao.txt').st_size == 0:
                arquivo_texto.write(tempo_decorrido)
            else:
                arquivo_texto.write('\n' + tempo_decorrido)
            arquivo_texto.close()
        else:
            duracao = open('duracao.txt', 'r')
            duracoes = duracao.readlines()
            duracoes[-1] = tempo_decorrido
            duracao = open('duracao.txt', 'w')
            duracao.writelines(duracoes)
            duracao.close()

    def atualizaMovimentos(movimento, duracao):
        '''
        Esta função adiciona o movimento mais recente a lista de movimentos da partida atual.
        As partidas são salvas no histórico no formato: [movimentos = [A-B,B-C,C-A, ...], vitoria = False]
        '''

        historico = open('historico.txt', 'r')
        partidas = historico.readlines()
        partida_atual = partidas[-1]
        lista_partida = ast.literal_eval(partida_atual)
        lista_partida[0].append(movimento)
        partidas[-1] = str(lista_partida)
        historico = open('historico.txt', 'w')
        historico.writelines(partidas)
        historico.close()
        Arquivos.atualizaDuracao(duracao)

    def registraLog(texto):

        ''' Esta função adiciona as informações de uma exceção à ultima linha do arquivo de log. '''

        arquivo_texto = open('log.txt', 'a+')
        if os.stat(os.getcwd() + chr(92) + 'log.txt').st_size == 0:
            arquivo_texto.write(ctime() + ' ' + texto)
        else:
            arquivo_texto.write('\n' + ctime() + ' ' + texto)
        arquivo_texto.close()

    def getAtributos():
        """
            Esta função estática (chamada sempre através de Arquivos.getAtributos()) retorna um
            conjunto com os nomes dos atributos desta classe.

            (None) -> set
        """
        return __atributos

    def getMetodos():
        """
            Esta função estática (chamada sempre através de Arquivos.getMetodos()) retorna um
            conjunto com os nomes dos métodos desta classe.

            (None) -> set
        """
        return __metodos

    def getManual():
        """
            Esta função estática (chamada sempre através de Arquivos.getManual()) retorna um
            dicionário que mapeia os nomes dos atributos e métodos às suas descrições.
            (None) -> dict
        """
        manual = dict()
        manual['Arquivos'] = Arquivos.__doc__
        manual['registraHistorico'] = Arquivos.registraHistorico.__doc__
        manual['atualizaMovimentos'] = Arquivos.atualizaMovimentos.__doc__
        manual['atualizaDuracao'] = Arquivos.atualizaDuracao.__doc__
        manual['registraLog'] = Arquivos.registraLog.__doc__
        manual['getManual'] = Arquivos.getManual.__doc__
        manual['getAtributos'] = Arquivos.getAtributos.__doc__
        manual['getMetodos'] = Arquivos.getMetodos.__doc__
        return manual

