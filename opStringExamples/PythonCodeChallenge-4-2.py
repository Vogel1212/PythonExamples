# course challenge 25
# Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.

name = str(input('Enter your full name: ')).strip()
print('Does your name have Silva? ', end='')
print('silva' in name.lower())