# Python challenge - dictated by Wolfgang, code developed by Gabriel
# Qual será seu salario em tres anos, se estivesse aumentado pra 10% a cada 3 meses.

sal = int(input('Qual é o salário mensal do funcionario? R$'))
perc = int(input('Quantos Porcento de aumento trimestral?: '))
anos = int(input('Em quantos anos esse cálculo deve ser feito?: '))
c1 = anos*12/3
calc = sal*(perc/100)
total = calc+sal*c1
calcfim = total-sal
print('Salário antigo do funcionario era R${:.2f}, agora com {}% de aumento trimestral durante {} anos, vai passar a ganhar R${:.2f} por mês.\nCom um aumento de R${:.2f} após 3 anos'.format(sal,perc,anos,total,calcfim))