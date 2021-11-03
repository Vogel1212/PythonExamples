# 3.1. Using Python as a Calculator
# https://docs.python.org/3/tutorial/introduction.html#using-python-as-a-calculator

n1 = float(input('First number: '))
n2 = float(input('Second number: '))

print(f'{n1} + {n2} = {n1+n2}')
print(f'{n1} - {n2}*6 = {(n1-n2) * 6}')
print(f'({n2} - {n2}) / 4 = {(n1-n2) // 4}')
print(f'{n1} / {n2} = {n1 // n2}')