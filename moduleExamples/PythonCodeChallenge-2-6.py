# course challenge 18
# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

import math

ang = float(input('Enter an Angle: '))

seno = math.sin(math.radians(ang))
coss = math.cos(math.radians(ang))
tang = math.tan(math.radians(ang))

print('angle of {} has the SINE of {:.2f}'.format(ang, seno))
print('angle of {} has the COSINE of {:.2f}'.format(ang, coss))
print('angle of {} has the TANGENT of {:.2f}'.format(ang, tang))