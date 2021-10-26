# course challenge 62
# Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos.

#print('TERMS OF A ARITHMETIC PROGRESSION')
#print('-=' * 10)
#first = int(input('First Term: '))
#reason = int(input('Reason of A.P: '))
#term = first
#cont = 1
#total = 0
#more = 10
#while more != 0:
#    total = total + more
#    while cont <= total:
#        print('{} → '.format(term), end='')
#        term += reason
#        cont += 1
#    print('BREAK')
#    mais = int(input('How many terms do you want to show more? '))
#print('Progression ended with {} terms shown'.format(total))

a = int(input('First Term: '))
b = int(input('Reason of A.P: '))
c = int(input('Enter the amount of terms of the A.P: '))
d = a
while d != (a+(b*c)):
    print(f'{d} → ', end='')
    d += b
print('BREAK')
x = 1
while x != 0:
    x = int(input('How many terms do you want to show more?: '))
    while d != (a+(b*(c+x))):
        print(f'{d} → ', end='')
        d += b
    c += x
    if x != 0:
        print('BREAK')
print(f'Progression ended with {((d-a)/b):.0f} terms shown.')
