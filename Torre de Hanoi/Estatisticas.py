import os
import ast
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure



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
        duracao = round(float(open('duracao.txt', 'r').readlines()[-1]),2)
        discos = lista_partida_atual[-2]
        if nro_movimentos < (2 ** discos) - 1:
            precisao = 0
        else:
            precisao = round(100 * ((2 ** discos) - 1) / nro_movimentos)
        if nro_movimentos == 0 and duracao == 0 and precisao == 0:
            return
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

    def criaGrafico(self,estatistica_y):
        """
        Cria um gráfico baseado nas estatísticas pedidas, onde estatistica_i pode ser: 0 (nro_movimentos), 1 (duração) e 2 (precisão).

        int -> sem retorno (Exibe gráfico)
        """
        dados = Estatisticas.arrayEstatisticas()
        n = np.shape(dados)[0]
        x = np.arange(1, n + 1)
        y = dados[:, estatistica_y]
        fig = Figure(figsize=(6,6),dpi=100)
        a = fig.add_subplot(111)
        labels = {0: 'Nº de Movimentos', 1: 'Duração (s)', 2: 'Precisão (%)'}
        a.plot(x, y, 'r')
        a.set_xlabel('Partida', labelpad = -198)
        a.set_ylabel(labels[estatistica_y], labelpad = -2)
        if int(round(n/16,0)) == 0:
            a.set_xticks(np.arange(1, n + 1 ,1))
        else:
            a.set_xticks(np.arange(1, n + 1, int(round(n/16,0))))
        polinomio_ticks = -7 * (estatistica_y ** 2) + 13 * (estatistica_y) + 4
        if polinomio_ticks == 2:
            a.set_yticks(np.arange(0, 101, 10))
        else:
            a.set_yticks(np.arange(min(y), max(y) + polinomio_ticks, polinomio_ticks))
        canvas = FigureCanvasTkAgg(fig, self)
        canvas.get_tk_widget().pack()
        canvas.draw()

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

