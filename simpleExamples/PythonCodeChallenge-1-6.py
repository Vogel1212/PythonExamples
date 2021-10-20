# course challenge 10
# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.

quant = float(input('Quanto de dinheiro você tem na carteira? R$'))
dolar = 5.58

print('Com R${:.2f} você pode comprar US${:.2f}'.format(quant, quant / dolar))