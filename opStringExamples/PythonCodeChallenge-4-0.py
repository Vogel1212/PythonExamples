# course challenge 23
# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.

n = int(input('Enter a number: '))
u = n // 1 % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10
print('Analyzing the number {}'.format(n))
print('Unit: {}'.format(u))
print('Ten: {}'.format(d))
print('Hundred: {}'.format(c))
print('Thousands: {}'.format(m))
