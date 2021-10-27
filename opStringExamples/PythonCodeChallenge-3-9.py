# course challenge 22
# Crie um programa que leia o nome completo de uma pessoa e mostre: 
# - O nome com todas as letras maiúsculas.
# - O nome com todas minúsculas.
# - Quantas letras ao todo (sem considerar espaços). 
# - Quantas letras tem o primeiro nome.

name = str(input('Enter your full name: '))
print('Analyzing your name...')
print('Your name in capital letters is {}'.format(name.upper()))
print('Your name in lowercase is {}'.format(name.lower()))
print('Your name has the whole {} letters'.format(name.__len__()))
print('Your first name has {} letters'.format(name.find(' ')))