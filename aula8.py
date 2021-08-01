# Utilizando módulos

# (import math) importa toda a biblioteca matemática
# (from math import sqrt) importa apenas o módulo sqrt
# (from math import sqrt, factorial) importa dois ou mais módulos

# from math import ceil Faz o arredondamento de uma nota para cima, ex: 7.25 se torna 8
# from math import floor Faz o arredondamento de uma nota para baixo, ex: 7.25 se torna 7
# from math import trunc Faz o arredondamento de uma nota para baixo, ex: 7.25 se torna 7
# from math import pow Funciona de forma semelhante aos dois asterisco (**)
# from math import sqrt Calculo da raiz quadrada
# from math import factorial Calculo de fatorial

from math import sqrt

num = int(input('Digite um número:'))
raiz = sqrt(num)
print('A raiz quadrada de {} é igual a {:.2f}'.format(num, raiz))
##############################################################################
import random

num = random.randint(1, 10)  # mostra números inteiros de 1 a 10
print(num)

##############################################################################

import emoji
print(emoji.emojize("Olá, Mundo :earth_americas:", use_aliases=True))