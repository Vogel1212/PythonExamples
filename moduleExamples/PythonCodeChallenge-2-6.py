# course challenge 18
# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

import math

ang = float(input('Digite um angulo: '))

seno = math.sin(math.radians(ang))
coss = math.cos(math.radians(ang))
tang = math.tan(math.radians(ang))

print('Angulo de {} tem o SENO de {:.2f}'.format(ang, seno))
print('Angulo de {} tem o COSSENO de {:.2f}'.format(ang, coss))
print('Angulo de {} tem o TANGENTE de {:.2f}'.format(ang, tang))