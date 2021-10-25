# internet challenge - wiki.python.org.br
# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
# Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, 
# faça um programa que nos dê:
# salário bruto.
# quanto pagou ao INSS.
# quanto pagou ao sindicato.
# o salário líquido.
# calcule os descontos e o salário líquido, conforme a tabela abaixo

ganho = int(input('Value earned per hour worked: US$'))
horas = int(input('How many hours did you work this month: US$'))
bruto = horas*ganho
ir = bruto*(11/100)
inss = bruto*(8/100)
sind = bruto*(5/100)
liq = bruto-ir-inss-sind


print('Gross salary: US${}'.format(bruto))
print('IR (11%): US${}'.format(ir))
print('INSS (8%): US${}'.format(inss))
print('Sindicato (5%): US${}'.format(sind))
print('Liquid Salary: US${}'.format(liq))