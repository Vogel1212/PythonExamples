# course challenge 19
# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.

from random import choice

a = str(input('First student: '))
b = str(input('Second student: '))
c = str(input('Third student: '))
d = str(input('Fourth student: '))

list = (a,b,c,d)
drawn = choice(list)

print('The chosen student was {}'.format(drawn))
