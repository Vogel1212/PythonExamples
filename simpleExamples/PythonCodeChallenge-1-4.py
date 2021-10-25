# course challenge 8
# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

meters = float(input('Enter a distance in meters: '))
print('the measure of {}m stands for:\n'.format(meters))
print('{:.0f}mm'.format(meters * 1000))
print('{:.0f}cm'.format(meters * 100))
print('{:.0f}dm'.format(meters * 10))
print('{}dam'.format(meters / 10))
print('{}hm'.format(meters / 100))
print('{}km'.format(meters / 1000))