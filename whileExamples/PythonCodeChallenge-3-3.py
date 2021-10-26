# course challenge 60
# Faça um programa que leia um número qualquer e mostre o seu fatorial.
# Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120

from math import factorial

#print('Digite um número para')
#n = int(input('Calcular seu Fatorial: '))
#f = factorial(n)
#print('O fatorial de {} é igual a: {}'.format(n,f))

n = int(input('Digite um numero para calcular seu Fatorial: '))
cont = n
fac = 1
print('Calculando {}! = '.format(n), end='')
while cont > 0:
    print('{}'.format(cont), end='')
    print(' x ' if cont > 1 else ' = ', end='')
    cont -= 1
print(factorial(n))
