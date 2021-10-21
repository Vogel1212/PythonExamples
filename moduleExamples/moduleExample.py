# aula 08 - ultilizando modulos
# raiz quadrada

#import math
import random
from math import sqrt
num = int(input('Digite um numero: '))
#raiz = math.sqrt(num)
raiz = sqrt(num)
print('A raiz de {} é igual a {:.2f}'.format(num, raiz))

n = random.randint(1,10)
print('Numero aleatorio:'.format(n))