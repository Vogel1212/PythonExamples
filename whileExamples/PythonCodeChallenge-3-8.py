# course challenge 65
# Crie um programa que leia vários números inteiros pelo teclado. 
# No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. 
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

p=1
sum=0
cont = larger = less = 0
while p==1:
    n=int(input('Enter some values: '))
    
    sum+=n
    cont+=1
    if n!=0:
        if n>p:
            larger=n
        else:
            less=p
        if n<p:
            less=n
        else:
            less=p
    p=int(input('Would you like to type any more values? 1=yes or 0=no:'))
print('The average of the values is {}.'.format(sum/cont))
print('The highest value read was {} and the smallest was {}'.format(larger, less))
print('The end')