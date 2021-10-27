# course challenge 27
# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

name = str(input('Enter your full name: '))
n = name.split()
print('Nice to meet you!')
print('Your first name is {}'.format(n[0]))
print('Your last name is {}'.format(n[len(n)-1]))