class CommandError(Exception):
    pass

class SaveNaoEncontradoError(Exception):
    pass

def verifica_interface(n):

    """
    Verifica se a opção escolhida pelo jogador na interface do usuário é valida (é um número entre
    1 e 5), caso não chama um CommandError;
    str -> sem retorno (chama CommandError em caso de entrada inadequada)

    """

    try:
        if int(n) not in range(1,6):
            raise CommandError
    except ValueError:
        raise CommandError

def verifica_discos(disco_topo_saida,disco_topo_entrada):

    """

    Verifica se os discos do topo dos pinos escolhidos pelo jogador são adequados para a jogada ,se ele não está
    tentando colocar um disco maior em cima de um menor ou tentanto retirar o disco de uma torre sem discos, caso
    um desses erros seja detectado chama um CommandError;

    int,int -> sem retorno (chama CommandError em caso de entrada inadequada)

    """

    if (disco_topo_saida > disco_topo_entrada) or disco_topo_saida == 0:
        raise CommandError

def verifica_pinos(pino_retirada,pino_recebe):

    try:

        if int(pino_retirada) not in range(1,4):
            print('Você escolheu um número inválido para o pino de saida, escolha um número de 1 a 3!!!')
            raise CommandError
        elif int(pino_recebe) not in range(1, 4):
            print('Você escolheu um número inválido para o pino de entrada, escolha um número de 1 a 3!!!')
            raise CommandError
        elif int(pino_retirada) == int(pino_recebe):
            print('Você tentou mover um disco de um pino para ele mesmo, jogada inválida!!!')
            raise CommandError

    except ValueError:
        raise CommandError


def verifica_graf(y):

    """

    Verifica se o usuário informou um número válido para a criação de um gráfico de estatísticas;
    str -> sem retorno (chama CommandError em caso de entrada inadequada)

    """

    if y not in ('1','2','3','4'): raise CommandError
    pass


def verifica_save():

    """

    Verifica se existe um jogo salvo para ser aberto na opção "Carregar jogo", caso não chama SaveNaoEncontradoError;
    sem entrada -> sem retorno (chama SaveNaoEncontradoError em caso de inadequação')

    """

    try:
        a = open('historico.txt')
        a.close()
    except FileNotFoundError:
        print('Arquivo de save não encontrado, começando novo jogo')
        raise SaveNaoEncontradoError

manual_excecoes = dict()
manual_excecoes['verifica_interface']              = verifica_interface.__doc__
manual_excecoes['verifica_discos']                 = verifica_discos.__doc__
manual_excecoes['verifica_graf']                   = verifica_interface.__doc__
manual_excecoes['verifica_save']                   = verifica_save.__doc__
