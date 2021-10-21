# course challenge 17
# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.

import math

print('Calculando Hipotenusa')
opo = float(input('Medita do cateto oposto: '))
adja = float(input('Medida do cateto adjacente: '))

#hipo = (opo ** 2) + (adja ** 2)
#hipo = math.sqrt(hipo)

hipo = math.hypot(opo, adja)

print('A Hipotenusa desse triângulo é: {:.2f}'.format(hipo))
