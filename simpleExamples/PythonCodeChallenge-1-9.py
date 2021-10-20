# course challenge 13
# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

sal = int(input('Qual é o salário do funcionario? R$'))
perc = int(input('Quantos Porcento de aumento?: '))
calc = sal*(perc/100)
total = calc+sal
print('Salário antigo do funcionario era R${:.2f}, agora com {}% de aumento, passa a ganhar R${:.2f} por mês.\nCom um aumento de R${}'.format(sal,perc,total,calc))