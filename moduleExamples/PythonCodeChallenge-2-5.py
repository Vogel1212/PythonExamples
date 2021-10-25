# course challenge 17
# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.

import math

print('Calculating Hypotenuse')
opo = float(input('Measure of the opposite leg: '))
adja = float(input('Adjacent collar measurement: '))

#hipo = (opo ** 2) + (adja ** 2)
#hipo = math.sqrt(hipo)

hipo = math.hypot(opo, adja)

print('The hypotenuse of this triangle is: {:.2f}'.format(hipo))
