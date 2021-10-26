# course challenge 60
# Faça um programa que leia um número qualquer e mostre o seu fatorial.
# Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120

from math import factorial

#print('Enter a number for')
#n = int(input('Calculate your factorial: '))
#f = factorial(n)
#print('the factorial of {} its the same as: {}'.format(n,f))

n = int(input('Enter a number to calculate your factorial: '))
cont = n
fac = 1
print('calculating {}! = '.format(n), end='')
while cont > 0:
    print('{}'.format(cont), end='')
    print(' x ' if cont > 1 else ' = ', end='')
    cont -= 1
print(factorial(n))
