from tkinter import messagebox

class CommandError(Exception):
    pass

class SaveNaoEncontradoError(Exception):
    pass

class Erros:

    __metodos = {'verifica_jogada', 'entrada_disco', 'verifica_save','getAtributos','getMetodos','getManual'}
    __atributos = {}

    def verifica_jogada(pino_retirada,pino_recebe):
        '''
           Verifica se a opção escolhida pelo jogador é válida.
        '''
        if pino_retirada == pino_recebe:
            raise CommandError
        if len(pino_retirada) == 0:
            raise CommandError
        if pino_recebe != [] and (min(pino_retirada) > min(pino_recebe)):
            raise CommandError

    def entrada_disco(n_discos):
        '''
           Verifica se o número de discos fornecido pelo jogador é válido
        '''
        try:
            n_discos = int(n_discos)
            if n_discos>10 or n_discos<3:
                raise CommandError
        except ValueError:
            raise CommandError
        except TypeError:
            raise CommandError

    def verifica_save():

        """

        Verifica se existe um jogo salvo para ser aberto na opção "Carregar jogo", caso não chama SaveNaoEncontradoError;
        sem entrada -> sem retorno (chama SaveNaoEncontradoError em caso de inadequação')

        """
        try: 
            historico = open('historico.txt', 'r')
        except FileNotFoundError:
            raise SaveNaoEncontradoError

    def getAtributos():
        """
            Esta função estática (chamada sempre através de Erros.getAtributos()) retorna um
            conjunto com os nomes dos atributos desta classe.

            (None) -> set
        """
        return __atributos

    def getMetodos():
        """
            Esta função estática (chamada sempre através de Erros.getMetodos()) retorna um
            conjunto com os nomes dos métodos desta classe.

            (None) -> set
        """
        return __metodos

    def getManual():
        """
            Esta função estática (chamada sempre através de Erros.getManual()) retorna um
            dicionário que mapeia os nomes dos atributos e métodos às suas descrições.
            (None) -> dict
        """
        manual = dict()
        manual['Erros'] = Erros.__doc__
        manual['verifica_jogada'] = Erros.registraHistorico.__doc__
        manual['entrada_disco'] = Erros.atualizaMovimentos.__doc__
        manual['verifica_save'] = Erros.atualizaDuracao.__doc__
        manual['getManual'] = Erros.getManual.__doc__
        manual['getAtributos'] = Erros.getAtributos.__doc__
        manual['getMetodos'] = Erros.getMetodos.__doc__
        return manual