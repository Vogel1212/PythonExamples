# course challenge 25
# Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.

name = str(input('Digite seu nome completo: ')).strip()
print('Seu nome tem Silva? ', end='')
print('silva' in name.lower())