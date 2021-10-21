# course challenge 15
# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. 
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

dias = int(input('Quantos dias de Aluguel? '))
km = float(input('Quantos Km foram rodados? '))
diascont = dias * 60
kmcont = km * 0.15
tt = diascont+kmcont


print('Total a pagar: R${:.2f}'.format(tt))