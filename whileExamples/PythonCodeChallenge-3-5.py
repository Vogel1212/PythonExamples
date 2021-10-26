# course challenge 62
# Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos.
        
        
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
