# course challenge 20
# O mesmo professor do desafio 019 quer sortear a ordem de apresentação de trabalhos dos alunos. 
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

import random

a = str(input('First student: '))
b = str(input('Second student: '))
c = str(input('Third student: '))
d = str(input('Fourth student: '))

list = [a,b,c,d]
random.shuffle(list)

print('The order of presentation will be:')
print(list)
