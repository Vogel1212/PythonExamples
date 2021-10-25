# Python challenge - dictated by Wolfgang, code developed by Gabriel
# Qual será seu salario em tres anos, se estivesse aumentado pra 10% a cada 3 meses.

sal = int(input('What is the employees monthly salary? US$'))
perc = int(input('How many percent quarterly increase?: '))
years = int(input('How many years should this calculation take?: '))
c1 = years*12/3
calc = sal*(perc/100)
total = calc+sal*c1
calcfim = total-sal
print('The employees old salary was US${:.2f}, now with {}% of quarterly increase during {} years, will start to win US${:.2f} a month.\nWith an increase of US${:.2f} after 3 years'.format(sal,perc,years,total,calcfim))