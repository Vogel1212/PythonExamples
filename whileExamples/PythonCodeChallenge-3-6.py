# course challenge 63
# Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci. 
# Ex: 0 - 1 - 1 - 2 - 3 - 5 - 8

print('-' * 20)
print('Fibonacci Sequence')
print('-' * 20)

terms = int(input('How many terms do you want to show? '))
cont = 1
ant = 0
prox = 1
sum = 1

print('~'*40)
while cont <= terms:
    print(ant, end='-')
    cont += 1
    sum = prox + ant
    ant = prox
    prox = sum
print('The end.')