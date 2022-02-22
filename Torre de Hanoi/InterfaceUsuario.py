import os
os.system("color")

class InterfaceUsuario:
    """
        Super classe que contém todos os métodos e atributos que sejam úteis pra qualquer
        interface que possa ser feita com o usuário.
    """
    
    def __init__(self):
        """
            Inicializador da classe. Inicializa um dicionario que associa os indices de 0 a
            255 (inclusive) a todos os primeiros 256 caracteres que o cmd do windows reconhece.
            Tambem seta os atributos das cores ANSI. Eles são úteis para escrever caracteres 
            coloridos.

            Adaptado de https://www.codegrepper.com/code-examples/python/python+ansi+colors
            Acesso em 09/01/2022
        """
        self.pref = "\033["
        self.reset = f"{self.pref}0m"
        self.black = "30m"
        self.red = "31m"
        self.green = "32m"
        self.yellow = "33m"
        self.blue = "34m"
        self.magenta = "35m"
        self.cyan = "36m"
        self.white = "37m"
        
    def strANSI(text, color=None, is_bold=False):
        """
            Retorna a string 'text' na cor setada por 'color' e 'is_bold'.
        """
        if color == None or color.upper() == "WHITE": color = self.white
        elif color.upper() == "BLACK": color = self.black
        elif color.upper() == "RED": color = self.red
        elif color.upper() == "GREEN": color = self.green
        elif color.upper() == "YELLOW": color = self.yellow
        elif color.upper() == "BLUE": color = self.blue
        elif color.upper() == "MAGENTA": color = self.magenta
        elif color.upper() == "CYAN": color = self.cyan
        else: color == self.white
        return f'{self.pref}{1 if is_bold else 0};{color}' + text + self.reset
        
    def print(self,text, color=None, is_bold=False):
        """
            Printa na tela a string 'text' na cor setada por 'color' e 'is_bold'.
        """
        if color == None or color.upper() == "WHITE": color = self.white
        elif color.upper() == "BLACK": color = self.black
        elif color.upper() == "RED": color = self.red
        elif color.upper() == "GREEN": color = self.green
        elif color.upper() == "YELLOW": color = self.yellow
        elif color.upper() == "BLUE": color = self.blue
        elif color.upper() == "MAGENTA": color = self.magenta
        elif color.upper() == "CYAN": color = self.cyan
        else: color == self.white
        print(f'{self.pref}{1 if is_bold else 0};{color}' + text + self.reset)

    def limpa_tela():

        """ Limpa a tela do cmd; sem entrada -> sem retorno """

        os.system('cls') or None

    def simbolos(simb):

        """
        Função para usar simbolos no python (quadrado, estrela, etc);
        str -> str
        """
        simbolos = {'estrela':'★','quadrado':'☐','emoji_triste':'☹','emoji_feliz':'☺','seta_dir':'⇾','seta_esq':'⇽'}
        return simbolos[simb]


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
        manual['__init__']              = InterfaceUsuario.__init__.__doc__
        manual['strANSI']               = InterfaceUsuario.strANSI.__doc__
        manual['limpa_tela']            = InterfaceUsuario.limpa_tela.__doc__
        manual['simbolos']              = InterfaceUsuario.simbolos.__doc__
        manual['print']                 = InterfaceUsuario.print.__doc__
        manual['getManual']             = InterfaceUsuario.getManual.__doc__
        manual['getAtributos']          = InterfaceUsuario.getAtributos.__doc__
        manual['getMetodos']            = InterfaceUsuario.getMetodos.__doc__
        return manual

