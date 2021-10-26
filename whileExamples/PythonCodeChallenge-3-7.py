# course challenge 64
# Crie um programa que leia vários números inteiros pelo teclado. 
# O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. 
# No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).
# https://www.youtube.com/watch?v=mYlbttiLHM0&list=PLvE-ZAFRgX8hnECDn1v9HNTI71veL3oW0&index=80

n = int(input('Enter a number [enter 999 to stop]: '))
stop = 999
s = n

while s <= stop:
    b = int(input('Enter a number [enter 999 to stop]: '))
print('You typed {} numbers and the sum between them was {}')

# >>> Falta terminar