import os
import ast
import numpy as np
import matplotlib.pyplot as plt


class Estatisticas:
    """
    Classe que contem todos os metodos que podem ser úteis na criação e manipulação de estatísticas e gráficos.
    """

    __metodos = {'atualizaEstatisticas', 'arrayEstatisticas', 'criaGrafico', 'getAtributos', 'getMetodos', 'getManual'}

    def atualizaEstatisticas():
        """
        Esta função cria as estatísticas relevantes da última partida do histórico e das durações e as copia para o arquivo de estatísticas.
        No formato: [nro de movimentos, duração, precisão];

        sem entrada -> sem retorno (Atualiza arquivo)

        """

        partida_atual = open('historico.txt', 'r').readlines()[-1]
        lista_partida_atual = ast.literal_eval(partida_atual)
        estatisticas_partida = []
        nro_movimentos = len(lista_partida_atual[0])
        duracao = open('duracao.txt', 'r').readlines()[-1]
        movs_solucao = lista_partida_atual[-1]
        precisao = round(100 * ((2 ** movs_solucao) - 1) / nro_movimentos)
        estatisticas_partida.append(nro_movimentos)
        estatisticas_partida.append(duracao)
        estatisticas_partida.append(precisao)
        estatisticas = open('estatisticas.txt', 'a+')
        if os.stat(os.getcwd() + chr(92) + 'estatisticas.txt').st_size == 0:
            estatisticas.write(str(estatisticas_partida))
        else:
            estatisticas.write('\n' + str(estatisticas_partida))
        estatisticas.close()



    def arrayEstatisticas():
        """
        Cria um array (nx3) a partir das informações das n partidas do arquivo de estatísticas.

        sem entrada -> numpy.array
        """
        estatisticas = open('estatisticas.txt', 'r').readlines()
        lista_estatisticas = []
        for partida in estatisticas[:-1]:
            lista_estatisticas.append(ast.literal_eval(partida[:-1]))
        lista_estatisticas.append(ast.literal_eval(estatisticas[-1]))
        array_estatisticas = np.array([np.array(linha) for linha in lista_estatisticas], 'int32')
        return array_estatisticas


    def criaGrafico(estatistica_y):
        """
        Cria um gráfico baseado nas estatísticas pedidas, onde estatistica_i pode ser: 0 (nro_movimentos), 1 (duração) e 2 (precisão).

        int -> sem retorno (Exibe gráfico)
        """

        dados = Estatisticas.arrayEstatisticas()
        n = np.shape(dados)[0]
        fig, ax = plt.subplots()
        x = np.arange(1, n + 1)
        y = dados[:, estatistica_y]
        labels = {0: 'Nro Movimentos', 1: 'Duração (s)', 2: 'Precisão (%)'}
        ax.plot(x, y, 'ro')
        plt.xlabel('Partida')
        plt.ylabel(labels[estatistica_y])
        ax.set_xticks(np.arange(1, n + 1, 1))
        polinomio_ticks = -7 * (estatistica_y ** 2) + 13 * (estatistica_y) + 4
        if polinomio_ticks == 2:
            ax.set_yticks(np.arange(0, 101, 10))
        else:
            ax.set_yticks(np.arange(min(y), max(y) + polinomio_ticks, polinomio_ticks))
        plt.show()



    def getAtributos():
        """
            Esta função estática (chamada sempre através de Estatisticas.getAtributos()) retorna um
            conjunto com os nomes dos atributos desta classe.

            (None) -> set
        """
        return __atributos

    def getMetodos():
        """
            Esta função estática (chamada sempre através de Estatisticas.getMetodos()) retorna um
            conjunto com os nomes dos métodos desta classe.

            (None) -> set
        """
        return __metodos

    def getManual():
        """
            Esta função estática (chamada sempre através de Estatisticas.getManual()) retorna um
            dicionário que mapeia os nomes dos atributos e métodos às suas descrições.
            (None) -> dict
        """
        manual = dict()
        manual['Estatisticas'] = Estatisticas.__doc__
        manual['atualizaEstatisticas'] = Estatisticas.atualizaEstatisticas.__doc__
        manual['arrayEstatisticas'] = Estatisticas.arrayEstatisticas.__doc__
        manual['criaGrafico'] = Estatisticas.atualizaEstatisticas.__doc__
        manual['getManual'] = Estatisticas.getManual.__doc__
        manual['getAtributos'] = Estatisticas.getAtributos.__doc__
        manual['getMetodos'] = Estatisticas.getMetodos.__doc__
        return manual

