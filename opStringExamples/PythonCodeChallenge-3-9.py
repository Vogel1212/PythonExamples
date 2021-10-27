# course challenge 22
# Crie um programa que leia o nome completo de uma pessoa e mostre: 
# - O nome com todas as letras maiúsculas.
# - O nome com todas minúsculas.
# - Quantas letras ao todo (sem considerar espaços). 
# - Quantas letras tem o primeiro nome.

name = str(input('Enter your full name: '))
print('Analisando seu nome...')
print('Seu nome em maiúsculas é {}'.format(name.upper()))
print('Seu nome em minúsculas é {}'.format(name.lower()))
print('Seu nome tem ao todo {} letras'.format(name.__len__()))
print('Seu primeiro nome tem {} letras'.format(name.find(' ')))