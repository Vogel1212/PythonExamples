# course challenge 26
# Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A", em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

ph = str(input('Digite uma frase:')).upper().strip()
print('A letra A aparece {} vezes na frase.'.format(ph.count('A')))
print('A primeira letra A apareceu na posição {}'.format(ph.find('A')+1))
print('A última letra A apareceu na posição {}'.format(ph.rfind('A')+1))