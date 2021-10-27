# course challenge 26
# Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A", em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

ph = str(input('Type a phrase:')).upper().strip()
print('The letter A appears {} times in the sentence.'.format(ph.count('A')))
print('The first letter A appears in position {}'.format(ph.find('A')+1))
print('The last letter A appears in the position {}'.format(ph.rfind('A')+1))