# course challenge 11
# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, 
# sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

alt = float(input('wall height: '))
larg = float(input('wall width: '))
wall = alt * larg
print('Your wall has the dimension of {}x{} and your area is {}m².'.format(alt, larg, wall))

ink = wall / 2
print('To paint this wall, you will need {}l of ink'.format(ink))