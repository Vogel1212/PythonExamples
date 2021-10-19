# course challenge 9
#  Faça um programa que leia um número Inteiro qualquer e mostre na tela a sua tabuada.

num = int(input('Digite um numero para ver sua tabuada: '))
for x in range(1, 11):
    print(f'{num :2} x {x :2} = {num * x :2}')