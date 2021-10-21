# internet challenge - wiki.python.org.br
# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
# Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, 
# faça um programa que nos dê:
# salário bruto.
# quanto pagou ao INSS.
# quanto pagou ao sindicato.
# o salário líquido.
# calcule os descontos e o salário líquido, conforme a tabela abaixo

ganho = int(input('Valor ganho por hora trabalhada: R$'))
horas = int(input('Quantas horas trabalhou esse mês: R$'))
bruto = horas*ganho
ir = bruto*(11/100)
inss = bruto*(8/100)
sind = bruto*(5/100)
liq = bruto-ir-inss-sind


print('Salário Bruto: R${}'.format(bruto))
print('IR (11%): R${}'.format(ir))
print('INSS (8%): R${}'.format(inss))
print('Sindicato (5%): R${}'.format(sind))
print('Salário Liquido: R${}'.format(liq))