# course challenge 13
# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

sal = int(input('What is the employees salary? US$'))
perc = int(input('How many percent increase?: '))
calc = sal*(perc/100)
total = calc+sal
print('The employees old salary was US${:.2f}, now with {}% of raise, starts to win US${:.2f} a month.\nWith an increase of US${}'.format(sal,perc,total,calc))