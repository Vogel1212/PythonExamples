# course challenge 61
# Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.

#Desafio 51
#print('-=' * 15)
#print('10 TERMS OF A ARITHMETIC PROGRESSION')
#print('-=' * 15)
#first = int(input('enter the first term: '))
#reason = int(input('What is the reason for the arithmetic progression: '))
#tenth = first + 10 * reason
#for c in range (first, tenth, reason):
#    print(c, end = ' → ')
#print('HE FINISHED')

print('TERMS OF A ARITHMETIC PROGRESSION')
print('-=' * 10)
first = int(input('First Term: '))
reason = int(input('Reason of A.P: '))
term = first
cont = 1
while cont <= 10:
    print('{} → '.format(term), end='')
    term += reason
    cont += 1
print('The end.')