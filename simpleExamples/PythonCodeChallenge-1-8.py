# course challenge 12
# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

price = float(input('How much does the product cost? US$'))
percent = int(input('How many percent off?: '))
calc = (price/100)*percent
sum = price-calc
print('The product that cost {:.2f}, with the discount coupon from {}% it will cost US${:.2f}'.format(price,percent,sum))
print('You won US${:.2f}, discount'.format(price-sum))