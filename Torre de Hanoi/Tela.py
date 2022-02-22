from InterfaceUsuario import *
from Exceções import *
from Arquivos import *
from Estatisticas import *


class Tela(InterfaceUsuario):
    """
        Esta classe representa a tela que é mostrada ao usuário. Todas a telas apresentadas são métodos da
        classe Tela.
    """
    __atributos     = {}
    __metodos       = {'__init__','__str__','desenhaTela','getOpcaoEscolhida','getManual','getAtributos','getMetodos'}

    
    def getOpcaoEscolhida(self):
        """
            Esta função lê a opção escolhida pelo usuário a partir do console e retorna
            a escolha.
            
            (Tela) -> int
        """        
        return -1

    def menuPrincipal():
        """
           Apresenta na tela para o usuário as opções do menu principal
           (Novo Jogo, Carregar Jogo, Opções, Manual do Desenvolvedor, Estatísticas)

           (None) -> (None)
        """

        Tela.limpa_tela()

        print('\n             MENU PRINCIPAL          \n\n')
        print('\nNovo Jogo [1]')
        print('\nCarregar Jogo [2]')
        print('\nOpções [3]')
        print('\nManual do Desenvolvedor [4]')
        print('\nEstatísticas [5]')
        entrada = (input('\nEscolha a opção desejada: '))

        try:
            verifica_interface(entrada)
        except CommandError:
            print('\nO valor informado nao é valido, informe um dos número apresentados na tela')
            erro = 'Erro: o Usuario informou um valor inadequado no menu inicial, '
            msg = 'Mensagem de erro: O valor informado nao e válido, informe um dos número apresentados na tela, '
            trat = 'Tratamento do erro: Volta ao menu inicial para o usuario escolher outra opcao'
            Arquivos.registraLog(erro + msg + trat)
            input(' ===== Digite enter para escolher novamente =====')
            return None

        return entrada


    def TelaEstats():

        """ Apresenta para o usuário as opções do menu de estatísticas. """

        while True:

            Tela.limpa_tela()

            print('\n             Estatísticas         \n\n')

            print('Opções de gráfico para exibir: \n[1] nro_movimentos x partidas\n[2] duração x partidas\n[3] precisão x partidas\n[4] Voltar ao menu principal \n')
            print('\n*precisão = 100(nro_movimentos / nro_min_movimentos)\n')
            print('\n*Jogabilide em desenvolvimento, um arquivo "estatisticas.txt" de exemplo foi usado para visualizar os gráficos\n')
            graf = input('Gráfico escolhido: ')


            try:
                verifica_graf(graf)

                if graf == '4':
                    break

                else:

                    graf = int(graf) - 1
                    Estatisticas.criaGrafico(graf)

            except CommandError:
                print('Você informou um valor inválido para o gráfico, informe um valor entre 1 e 4 conferme indicado!!\n')
                erro = 'Erro: o Usuario informou um valor inadequado no menu de estatísticas, '
                msg = 'Mensagem de erro: O valor informado nao e válido, informe um dos número apresentados na tela, '
                trat = 'Tratamento do erro: Volta ao menu de estatísticas para o usuario escolher outra opcao'
                Arquivos.registraLog(erro + msg+ trat)
                input('\n ===== Digite enter para escolher novamente =====')
                pass


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
        manual['menuPrincipal']         = Tela.menuPrincipal.__doc__
        manual['TelaEstats']            = Tela.TelaEstats.__doc__
        manual['getManual']             = Tela.getManual.__doc__
        manual['getAtributos']          = Tela.getAtributos.__doc__
        manual['getMetodos']            = Tela.getMetodos.__doc__
        return manual
