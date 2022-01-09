"""
   Este program consiste no jogo Torre de Hanoi.

   "Torre de Hanói é um quebra-cabeça que consiste em uma base contendo três pinos, em um dos quais são
   dispostos alguns discos uns sobre os outros, em ordem crescente de diâmetro, de cima para baixo.

   O problema consiste em passar todos os discos de um pino para outro qualquer, usando um dos pinos como
   auxiliar, de maneira que um disco maior nunca fique em cima de outro menor em nenhuma situação.

   O número de discos pode variar sendo que o mais simples contém apenas três."
   - Fonte: https://pt.wikipedia.org/wiki/Torre_de_Han%C3%B3i

   Opções de costomização:
   - Quantidade de discos (padrão 3)
   - Com tempo ou sem tempo (padrão sem tempo)
   - Com ou sem limite de jogadas (padrão sem limite)

   O jogo será formado por uma base contendo 3 PINOS e o número de DISCOS escolhidos, representada como:

               |                          |                     |
               |                          |                     |
             □□□                        |                     |
           □□□□□                       |                     |
         □□□□□□□                      |                     |

   O jogador poderá realizar sucessivas jogadas, que consintem em mover o Disco do topo de um Pino para outro,
   até que o jogo se encerre.

"""

# Document properties
__author__ = ['Pedro_Henrique_Busin_Cambruzzi', 'Pedro_Henrique_de_Miranda_Pinto']
__copyright__ = 'Copyright_2022'
__credits__ = __author__
__license__ = 'GPL'
__version__ = '1.0.0'
__maintainer__ = 'Pedro Henrique Busin Cambruzzi'
__email__ = 'pedrobusin@poli.ufrj.br'
__status__ = 'Production'
