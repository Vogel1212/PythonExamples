# course challenge 12
# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

preco = float(input('Quanto custa o produto? R$'))
percent = int(input('Quantos Porcento de desconto?: '))
calc = (preco/100)*percent
conta = preco-calc
print('O Produto que custava {:.2f}, com o cupom de desconto de {}% vai custar R${:.2f}'.format(preco,percent,conta))
print('Você ganhou R${:.2f} de desconto'.format(preco-conta))