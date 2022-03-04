from Exceções import *
from Arquivos import *
from Estatisticas import *
from tkinter import *
import tkinter.ttk as ttk
from TorreHanoi import *
import time

main = Tk()
main.geometry('480x320+490+120')
main.title('Torre de Hanoi')
main.resizable(False, False)
main.iconbitmap(os.getcwd()+chr(92)+'torre.ico')

class Tela:
    """
        Esta classe representa a tela que é mostrada ao usuário. Todas a telas apresentadas são métodos da
        classe Tela.
    """
    __atributos     = {'master'}
    __metodos       = {'__init__','limpa_frame','limpa_frame','menu_principal','estatisticas','tela_grafico','opcoes','manual','continuar_jogo','novo_jogo','tela_discos','tela_jogo','realiza_movimento_grafico','getManual','getAtributos','getMetodos'}

    def __init__(self, master):
        self.master = master
        master = Frame(main)
        master.pack()

    def limpa_frame(self):
        '''
           Limpa todos os widgets do frame
        '''
        for widget in self.master.winfo_children():
            widget.destroy()

    def menu_principal(self, resize = False):
        '''
           Mostra o menu principal ao usuário.
        '''
        if resize == True:
            main.geometry('480x320')
        self.limpa_frame()
        self.novojogo = Button(self.master, text = 'Novo Jogo', command = lambda: Tela.novo_jogo(self), font=('', 20), width = 20)
        self.novojogo.place(x = 75, y= 10)
        self.continuar = Button(self.master, text='Continuar Jogo', command = lambda: Tela.continuar_jogo(self), font=('', 20), width = 20)
        self.continuar.place(x = 75, y= 70)
        self.opcoes = Button(self.master, text='Opções', command = lambda: Tela.opcoes(self), font=('', 20), width = 20)
        self.opcoes.place(x = 75, y= 130)
        self.estatisticas = Button(self.master, text='Estatísticas', command = lambda: Tela.estatisticas(self), font=('', 20), width = 20)
        self.estatisticas.place(x = 75, y= 190)
        self.manual = Button(self.master, text='Manual do Desenvolvedor', command = lambda: Tela.manual(self), font=('', 20), width = 20)
        self.manual.place(x = 75, y= 250)

    def estatisticas(self):
        '''
           Mostra a tela de estatísticas ao usuário.
        '''
        try:
            estatisticas = open('estatisticas.txt')
        except:
            messagebox.showinfo(message='Não existe arquivo de estatísticas!')
            return
        self.limpa_frame()
        self.menu = Button(self.master, text = 'Nº de Movimentos x Partida', command = lambda: Tela.tela_grafico(self, 0), font=('', 20), width = 25)
        self.menu.place(x = 38, y=30)
        self.menu = Button(self.master, text = 'Duração x Partida', command = lambda: Tela.tela_grafico(self, 1), font=('', 20), width = 25)
        self.menu.place(x = 38, y=100)
        self.menu = Button(self.master, text = 'Precisão x Partida', command = lambda: Tela.tela_grafico(self, 2), font=('', 20), width = 25)
        self.menu.place(x = 38, y=170)
        self.menu = Button(self.master, text = 'Menu Principal', command = lambda: Tela.menu_principal(self))
        self.menu.place(x=195,y=280)

    def tela_grafico(self, n):
        '''
           Mostra a tela de escolha dos gráficos ao usuário.
        '''
        self.limpa_frame()
        self.voltar = Button(self.master, text = 'Voltar', command = lambda: Tela.estatisticas(self))
        self.voltar.pack(side='bottom')
        Estatisticas.criaGrafico(self.master,n)

    def opcoes(self):
        '''
           Mostra a tela de opções ao usuário.
        '''
        self.limpa_frame()
        self.cores = Label(self.master, text = 'Escolha a cor do fundo:', font = ('', 20))
        self.cores.place(x = 95, y = 20)
        self.cor_1 = Button(self.master, text = 'Amarelo', command = lambda: main.configure(bg ='yellow'), font = ('', 25), width = 8)
        self.cor_1.place(x = 67, y = 80)
        self.cor_2 = Button(self.master, text = 'Verde', command = lambda: main.configure(bg ='green'), font = ('', 25), width = 8)
        self.cor_2.place(x = 255, y = 80)
        self.cor_3 = Button(self.master, text = 'Azul', command = lambda: main.configure(bg ='blue'), font = ('', 25), width = 8)
        self.cor_3.place(x = 67, y = 180)
        self.cor_4 = Button(self.master, text = 'Cinza', command = lambda: main.configure(bg ='SystemButtonFace'), font = ('', 25), width = 8)
        self.cor_4.place(x = 255, y = 180)
        self.menu = Button(self.master, text = 'Menu Principal', command = lambda: Tela.menu_principal(self))
        self.menu.place(x = 190, y = 280)

    def manual(self):
        '''
           Mostra o manual de desenvolvedor ao usuário.
        '''
        self.limpa_frame()
        main.geometry('660x450')
        conteudo_manual = open('TorreHanoi.pyw', 'r', encoding="utf8").read()
        self.manual = Text(self.master)
        self.manual.insert('1.0', conteudo_manual)
        self.manual.grid(row=0, column=0)
        scroll_y = ttk.Scrollbar(self.master, command=self.manual.yview)
        scroll_y.grid(row=0, column=1, sticky='nsew')
        self.manual['yscrollcommand'] = scroll_y.set
        self.menu = Button(self.master, text = 'Menu Principal', command = lambda: Tela.menu_principal(self, True))
        self.menu.place(x=280, y=405)

    def continuar_jogo(self):
        '''
           Restaura um save anterior (caso exista) e encaminha o usuário a tela de jogo.
        '''
        if Arquivos.checa_status_partida() == True:
            messagebox.showinfo(message='Não existe jogo salvo!')
        else:
            estado = Arquivos.restaura_jogo()
            n = estado[2]
            Tela.tela_jogo(self,n, new_game = False)
            estado_atual = estado[0]
            lista_discos = []
            for torre in estado_atual:
                    for disco in torre:
                        lista_discos.append([disco, estado_atual.index(torre)])
            lista_discos_ordenada = sorted(lista_discos, key=lambda x: x[0])[::-1]
            global nro_movimentos_realizados
            nro_movimentos_realizados = [0,0,0]
            for disco in lista_discos_ordenada:
                self.realiza_movimento_grafico(disco[0], 0, disco[1], new_game = False)
                nro_movimentos_realizados[disco[1]] += 1

    def novo_jogo(self):
        '''
           Encaminha o usuário para um novo jogo.
        '''
        self.limpa_frame()
        self.instrucoes = Label(self.master, text = 'Insira o número de discos:', font = ('',15), anchor = 's')
        self.instrucoes.place(x = 115, y= 40)
        self.entrada = Entry(self.master)
        self.entrada.place(x = 175, y=90)
        self.ok = Button(self.master, text='OK', command=lambda: Tela.tela_discos(self, self.entrada.get()),font = ('',15))
        self.ok.place(x = 210, y =130)
        self.menu = Button(self.master, text = 'Voltar', command = lambda: Tela.menu_principal(self),font = ('',15))
        self.menu.place(x = 197, y= 180)

    def tela_discos(self,n):
        '''
           Pede para o usuário inserir com quantos discos deseja jogar.
        '''
        try:
            Erros.entrada_disco(n)
            Tela.tela_jogo(self, int(n))
        except CommandError:
            erro = 'Erro: CommandError'
            msg = 'Mensagem: Insira um inteiro entre 3 e 10!'
            trat = 'Tratamento do erro: Pede para o usuário inserir o número de discos novamente'
            Arquivos.registraLog(erro +' '+msg +' '+trat)
            messagebox.showinfo(message='Insira um inteiro entre 3 e 10!')
     
    def tela_jogo(self,n, new_game=True):
        '''
           Método para apresentação da gameplay.
        '''
        self.inicio = time.time()
        if new_game == True and Arquivos.checa_status_partida() == False:
            Estatisticas.atualizaEstatisticas()
        if new_game == True:
            Arquivos.registraHistorico(n)
        self.limpa_frame()
        self.canvas = c = Canvas(self.master)
        c.pack()
        largura, altura = main.getint(c['width']), main.getint(c['height'])
        #Gera Torres
        largura_torre = 10
        altura_torre = altura//2
        distancia_torre = largura//3
        x1, y1 = (distancia_torre-largura_torre)//2, altura*1//3
        x2, y2 = x1+largura_torre, y1+altura_torre
        self.torres = []
        p = c.create_rectangle(x1, y1, x2, y2, fill='black')
        self.torres.append(p)
        x1, x2 = x1+distancia_torre, x2+distancia_torre
        p = c.create_rectangle(x1, y1, x2, y2, fill='black')
        self.torres.append(p)
        x1, x2 = x1+distancia_torre, x2+distancia_torre
        p = c.create_rectangle(x1, y1, x2, y2, fill='black')
        self.torres.append(p)
        main.update()
        # Gera Discos 
        altura_disco = altura_torre//16
        largura_max_disco = distancia_torre*2//3
        largura_min_disco = 2*largura_torre
        self.estado_torre = [[], [], []]
        self.discos = {}
        x1, y1 = (distancia_torre-largura_max_disco)//2, y2-altura_disco-2
        x2, y2 = x1+largura_max_disco, y1+altura_disco
        dx = (largura_max_disco-largura_min_disco) // (2*max(1, n-1))
        for i in range(n, 0, -1):
            p = c.create_rectangle(x1, y1, x2, y2, fill='red')
            self.discos[i] = p
            self.estado_torre[0].append(i)
            x1, x2 = x1 + dx, x2-dx
            y1, y2 = y1 - altura_disco-2, y2-altura_disco-2
            main.update()
            main.after(25)
        # Botões de Interação
        menu = Button(self.master, text = 'Salvar e retornar ao menu principal',command = lambda: Tela.menu_principal(self))
        menu.place(x= 140,y = 10)#(x=194,y=10)
        self.informacoes = Label(self.master, text = 'Escolha uma torre:', font = ('', 12))
        self.informacoes.place(x=170,y=45)
        self.torre_1 = Button(self.master, text = 'Torre 1', font = ('', 16), command = lambda: TorreDeHanoi.interacao(self, 0, []))
        self.torre_1.pack(side='left',expand='yes')
        self.torre_2 = Button(self.master, text = 'Torre 2', font = ('', 16), command = lambda: TorreDeHanoi.interacao(self, 1, []))
        self.torre_2.pack(side='left',expand='yes')
        self.torre_3 = Button(self.master, text = 'Torre 3', font = ('', 16), command = lambda: TorreDeHanoi.interacao(self, 2, []))
        self.torre_3.pack(side='left', expand='yes')

    def realiza_movimento_grafico(self, i, a, b, new_game = True):
        '''
           Atualiza a GUI com o movimento que o usuário executou.
        '''
        del self.estado_torre[a][-1]
        p = self.discos[i]
        c = self.canvas
        # Levanta o disco na torre a
        ax1, ay1, ax2, ay2 = c.bbox(self.torres[a])
        while 1:
            x1, y1, x2, y2 = c.bbox(p)
            if y2 < ay1: break
            c.move(p, 0, -1)
            main.update()
        # Leva até a torre b
        bx1, by1, bx2, by2 = c.bbox(self.torres[b])
        novo_centro = (bx1+bx2)//2
        while 1:
            x1, y1, x2, y2 = c.bbox(p)
            centro = (x1+x2)//2
            if centro == novo_centro: break
            if centro > novo_centro: c.move(p, -1, 0)
            else: c.move(p, 1, 0)
            main.update()
        # Coloca sobre a peça que está na torre
        altura_disco = y2-y1
        if a != b:
            nova_base = by2 - altura_disco*len(self.estado_torre[b]) - 2
        else:
            nova_base = ay2 - altura_disco*nro_movimentos_realizados[a] - 2
        while 1:
            x1, y1, x2, y2 = c.bbox(p)
            if y2 >= nova_base: break
            c.move(p, 0, 1)
            main.update()
        # Atualiza o estado das torres
        self.estado_torre[b].append(i)
        main.update()
    
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
        manual['Tela']                          = Tela.__doc__
        manual['__init__']                      = Tela.__init__.__doc__
        manual['limpa_frame']                   = Tela.limpa_frame.__doc__
        manual['menu_principal']                = Tela.menu_principal.__doc__
        manual['estatisticas']                  = Tela.estatisticas.__doc__
        manual['tela_grafico']                  = Tela.tela_grafico.__doc__
        manual['opcoes']                        = Tela.opcoes.__doc__
        manual['manual']                        = Tela.manual.__doc__
        manual['continuar_jogo']                = Tela.continuar_jogo.__doc__
        manual['novo_jogo']                     = Tela.novo_jogo.__doc__
        manual['tela_discos']                   = Tela.tela_discos.__doc__
        manual['tela_jogo']                     = Tela.tela_jogo.__doc__
        manual['realiza_movimento_grafico']     = Tela.realiza_movimento_grafico.__doc__
        manual['getManual']                     = Tela.getManual.__doc__
        manual['getAtributos']                  = Tela.getAtributos.__doc__
        manual['getMetodos']                    = Tela.getMetodos.__doc__
        return manual


tela = Tela(main)
tela.menu_principal()

main.mainloop()
