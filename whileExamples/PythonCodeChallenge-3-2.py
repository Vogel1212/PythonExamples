# course challenge 59
# Crie um programa que leia dois valores e mostre um menu na tela:
# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.

n1 = int(input('First value: '))
n2 = int(input('Second value: '))
op = 0
while op != 5:
    print('=-=-=-=-=-=-=-=-=')
    print('[1] Sum\n[2] Multiply\n[3] Larger\n[4] New numbers\n[5] Exit the program')
    op = int(input('What is your option: '))
    print('=-=-=-=-=-=-=-=-=')
    if op == 1:
        print('The sum of {} + {} is: {}'.format(n1,n2,n1+n2))
    elif op == 2:
        print('{} x {} é: {}'.format(n1,n2,n1*n2))
    elif op == 3:
        if n1 > n2:
            print('Between {} and {}, the largest number is: {}'.format(n1,n2,n1))
        if n2 > n1:
            print('Between {} and {}, the largest number is: {}'.format(n1,n2,n2))
    elif op == 4:
        op = int(input('What is your option: '))
    elif op >= 6:
        print('Please enter a valid option!')
print('The end.')