import os

class Ferramentas:
    """
       Super classe que contem todos os metodos genéricos que podem ser úteis na mecânica do jogo.
    """

    __metodos = {'getAtributos', 'getMetodos', 'getManual'}

    def limpaTela():
        """
            Esta função limpa toda a tela do console do Windows. 
            Com isso, é possível dar 'refresh' na tela a ser desenhada.

            (None) -> (None)
        """
        os.system('cls')

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
        manual['Ferramnetas']             = Ferramentas.__doc__
        manual['getManual']               = Ferramentas.getManual.__doc__
        manual['getAtributos']            = Ferramentas.getAtributos.__doc__
        manual['getMetodos']              = Ferramentas.getMetodos.__doc__
        manual['limpaTela']               = Ferramentas.limpaTela.__doc__
        return manual
