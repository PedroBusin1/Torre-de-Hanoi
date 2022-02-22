class CommandError(Exception):
    pass

def verifica_interface(n):

    """ Verifica se a opção escolhida pelo jogador na interface do usuário é valida (é um número entre
    1 e 5), caso não chama um CommandError . """

    try:
        if int(n) not in range(1,6):
            raise CommandError
    except ValueError:
        raise CommandError

def verifica_discos(disco_topo_saida,disco_topo_entrada):

    """ Verifica se os discos do topo dos pinos escolhidos pelo jogador são adequados para a jogada ,se ele não está
     tentando colocar um disco maior em cima de um menor ou tentanto retirar o disco de uma torre sem discos, caso
     um desses erros seja detectado chama um CommandError """

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


def Verifica_graf(y):

    ''' Verifica se o usuário informou um número válido para a criação de um gráfico de estatísticas '''

    if y not in ('1','2','3','4'): raise CommandError
    pass
