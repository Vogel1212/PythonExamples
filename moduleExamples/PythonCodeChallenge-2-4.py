#course challenge 16
# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
# Ex: Digite um número: 6.127
# O número 6.127 tem a parte Inteira 6.

import math

num = float(input('Enter a number: '))
print('the value entered was {} and your entire portion is {}'.format(num, math.trunc(num)))
