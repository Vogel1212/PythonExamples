# course challenge 59
# Crie um programa que leia dois valores e mostre um menu na tela:
# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.
# https://www.youtube.com/watch?v=OBJL5vPj4-E&list=PLvE-ZAFRgX8hnECDn1v9HNTI71veL3oW0&index=75

n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
op = 0
while op != 5:
    print('=-=-=-=-=-=-=-=-=')
    print('[1] somar\n[2] multiplicar\n[3] maior\n[4] novos números\n[5] sair do programa')
    op = int(input('Qual é sua opção: '))
    print('=-=-=-=-=-=-=-=-=')
    if op == 1:
        print('A soma de {} + {} é: {}'.format(n1,n2,n1+n2))
    elif op == 2:
        print('{} x {} é: {}'.format(n1,n2,n1*n2))
    elif op == 3:
        if n1 > n2:
            print('Entre {} e {}, o maior numero é: {}'.format(n1,n2,n1))
        if n2 > n1:
            print('Entre {} e {}, o maior numero é: {}'.format(n1,n2,n2))
    elif op == 4:
        op = int(input('Qual é sua opção: '))
    elif op >= 6:
        print('Digite uma opção valida!')
print('The end.')