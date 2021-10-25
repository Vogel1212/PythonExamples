# aula 08 - ultilizando modulos
# raiz quadrada

#import math
import random
from math import sqrt
num = int(input('Enter a number: '))
#raiz = math.sqrt(num)
raiz = sqrt(num)
print('the root of {} its the same as {:.2f}'.format(num, raiz))

n = random.randint(1,10)
print('random number:'.format(n))