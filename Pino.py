import Disco

class Pino:
    """
       Classe que representa os pinos que contêm os discos no jogo.
    """

    __atributos    = {'discos'}
    __metodos      = {'__init__', '__str__', 'retira_disco', 'coloca_disco', 'getTamanhoPino', 'getManual', 'getAtributos', 'getMetodos'}

    def __init__(self,discos):
        """
           Metodo construtor, recebe uma lista de discos.

           (list[Disco]) -> Pino
        """
        self.discos = discos

    def __str__(self):
        """
           Método de representação visual do disco em string.

           (Pino) -> str
        """
        return None

    def retira_disco(self):
        """
           Retira e retorn o disco no topo (final da lista) do pino.

           (Disco) -> Disco
        """
        return None

    def coloca_disco(self,disco):
        """
           Adiciona um disco ao topo (final da lista) da pino.

           (Disco) -> Pino
        """
    def getTamanhoPino(self):
        """
           Retorna o número de discos no pino.

           (Pino) -> int
        """
        return None

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
        manual['Pino']                   = Pino.__doc__
        manual['__init__']               = Pino.__init__.__doc__
        manual['__str__']                = Pino.__str__.__doc__
        manual['retira_disco']           = Pino.retira_disco.__doc__
        manual['coloca_disco']           = Pino.coloca_disco.__doc__
        manual['getTamanhoPino']         = Pino.getTamanhoPino.__doc__
        manual['getManual']              = Pino.getManual.__doc__
        manual['getAtributos']           = Pino.getAtributos.__doc__
        manual['getMetodos']             = Pino.getMetodos.__doc__
        manual['discos']                 = '# lista dos discos no pino'
        return manual