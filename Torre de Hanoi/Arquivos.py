import os
import ast
from Exceções import *
from time import ctime


class Arquivos:
    """ Classe que contem todos os metodos que podem ser úteis na criação e atualização de arquivos. """

    __metodos = {'registraHistorico', 'atualizaMovimentos', 'atualizaDuracao', 'registraLog', 'altera_status_partida', 'checa_status_partida', 'restaura_jogo', 'getAtributos', 'getMetodos', 'getManual'}
    __atributos = {}

    def registraHistorico(nro_discos):

        """
        Esta função adiciona uma linha genérica a ultima linha do arquivo de histórico.
        As partidas são salvas no histórico no formato: [movimentos = [A-B,B-C,C-A, ...], vitoria = False, nro_discos, estado_jogo]

        int -> sem retorno (atualiza arquivos)
        """

        arquivo_texto = open('historico.txt', 'a+')
        if os.stat(os.getcwd() + chr(92) + 'historico.txt').st_size == 0:
            arquivo_texto.write('[[], False,' + str(nro_discos) +',[]'+ ']')
            Arquivos.atualizaDuracao('0', True)
        else:
            arquivo_texto.write('\n' + '[[], False,' + str(nro_discos) + ',[]'+']')
            Arquivos.atualizaDuracao('0', True)
        arquivo_texto.close()



    def atualizaDuracao(tempo_decorrido, nova_partida=False):

        """
        Esta função atualiza o arquivo com a duração das partidas até o último movimento feito.

        str -> sem retorno (Atualiza arquivo)
        """

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
            tempo_previo = duracoes[-1]
            duracoes[-1] = str(float(tempo_decorrido) + float(tempo_previo))
            duracao = open('duracao.txt', 'w')
            duracao.writelines(duracoes)
            duracao.close()



    def atualizaMovimentos(movimento, duracao, estado_atual):

        """
        Esta função adiciona o movimento mais recente a lista de movimentos da partida atual.

        str, str -> sem retorno (Atualiza os arquivos)
        """

        historico = open('historico.txt', 'r')
        partidas = historico.readlines()
        partida_atual = partidas[-1]
        lista_partida = ast.literal_eval(partida_atual)
        lista_partida[0].append(movimento)
        del lista_partida[-1]
        lista_partida.append(estado_atual)
        partidas[-1] = str(lista_partida)
        historico = open('historico.txt', 'w')
        historico.writelines(partidas)
        historico.close()
        Arquivos.atualizaDuracao(duracao)


    def altera_status_partida():
        '''
           Altera o estado de conclusão da partida salva para True (completa).
        '''
        historico = open('historico.txt', 'r')
        partidas = historico.readlines()
        partida_atual = partidas[-1]
        lista_partida = ast.literal_eval(partida_atual)
        lista_partida[1] = True
        partidas[-1] = str(lista_partida)
        historico = open('historico.txt', 'w')
        historico.writelines(partidas)
        historico.close()

    def checa_status_partida():
        '''
           Informa se existe uma partida salva para prosseguir o jogo.
        '''
        try:
            Erros.verifica_save()
            historico = open('historico.txt', 'r')
            partidas = historico.readlines()
            partida_atual = partidas[-1]
            lista_partida = ast.literal_eval(partida_atual)
            historico.close()
            if lista_partida[1] == True:
                raise SaveNaoEncontradoError
            else:
                return False
        except SaveNaoEncontradoError:
            erro = 'Erro: SaveNaoEncontradoError'
            msg = 'Mensagem: Não existe jogo salvo!'
            trat = 'Tratamento do erro: Retorna ao menu principal'
            Arquivos.registraLog(erro +' '+msg +' '+trat)
            return True
        

    def restaura_jogo():
        '''
           Resgata as informações necessárias do arquivo de save para prosseguir com o jogo.
        '''
        historico = open('historico.txt', 'r')
        partidas = historico.readlines()
        partida_atual = partidas[-1]
        lista_partida = ast.literal_eval(partida_atual)
        estado = lista_partida[-1]
        n_discos = int(lista_partida[-2])
        historico.close()
        duracao = open('duracao.txt', 'r')
        duracoes = duracao.readlines()
        tempo_partida = float(duracoes[-1])
        return (estado, tempo_partida, n_discos)


    def registraLog(texto):

        """
        Esta função adiciona as informações de uma exceção à ultima linha do arquivo de log;
        str -> sem retorno (Atualiza arquivo)

        """

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
        manual['altera_status_partida'] = Arquivos.altera_status_partida.__doc__
        manual['checa_status_partida'] = Arquivos.checa_status_partida.__doc__
        manual['restaura_jogo'] = Arquivos.restaura_jogo.__doc__
        manual['getManual'] = Arquivos.getManual.__doc__
        manual['getAtributos'] = Arquivos.getAtributos.__doc__
        manual['getMetodos'] = Arquivos.getMetodos.__doc__
        return manual

