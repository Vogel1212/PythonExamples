# course challenge 11
# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, 
# sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

alt = float(input('Altura da parede: '))
larg = float(input('Largura da parede: '))
parede = alt * larg
print('Sua parede tem a dimensão de {}x{} e sua área é de {}m².'.format(alt, larg, parede))

tinta = parede / 2
print('Para pintar essa parede, você precisará de {}l de tinta'.format(tinta))