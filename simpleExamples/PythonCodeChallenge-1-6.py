# course challenge 10
# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.

quant = float(input('How much money do you have in your wallet? R$'))
dolar = 5.68

print('With R${:.2f} you can buy US${:.2f}'.format(quant, quant / dolar))