class Disco:
    """
        Esta classe representa os discos da Torre de Hanoi. Os discos podem ter diferentes tamanhos e são movidos
        entre os pinos, para cima de outros discos de tamanho menor ou da base do pino.
    """

    __atributos   = {'tamanho'}
    __metodos     = {'__init__', '__str__', 'getTamanho','getManual','getAtributos','getMetodos'}

    def __init__(self, tamanho):
        """
           Metodo construtor, recebe o tamanho do disco.

           (int) -> disco
        """
        self.tamanho = tamanho

    def __str__(self):
        """
           Método de representação visual do disco em string.

           (disco) -> str
        """
        return

    def getTamanho(self):
        """
           Retorna o tamanho da pilha.

           (disco) -> str
        """
        return self.tamanho

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
        manual['Disco']                 = Disco.__doc__
        manual['__init__']              = Disco.__init__.__doc__
        manual['__str__']               = Disco.__str__.__doc__
        manual['getTamanho']            = Disco.getTamanho.__doc__
        manual['getManual']             = Disco.getManual.__doc__
        manual['getAtributos']          = Disco.getAtributos.__doc__
        manual['getMetodos']            = Disco.getMetodos.__doc__
        manual['tamanho']               = '# tamanho do disco'
        return manual
