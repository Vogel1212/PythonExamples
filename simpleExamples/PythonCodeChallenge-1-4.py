# course challenge 8
# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

metros = float(input('Digite uma distância em metros: '))
print('A medida de {}m corresponde a:\n'.format(metros))
print('{:.0f}mm'.format(metros * 1000))
print('{:.0f}cm'.format(metros * 100))
print('{:.0f}dm'.format(metros * 10))
print('{}dam'.format(metros / 10))
print('{}hm'.format(metros / 100))
print('{}km'.format(metros / 1000))