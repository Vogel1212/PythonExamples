# 3.1. Using Python as a Calculator
# 3.1.1. Numbers
# https://docs.python.org/3/tutorial/introduction.html#using-python-as-a-calculator

n1 = float(input('First number: '))
n2 = float(input('Second number: '))

width = int(input('Widht: '))
height = int(input('Height: '))

print('~'*30)

print(f'{n1} + {n2} = {n1+n2}')
print(f'{n1} - {n2}*6 = {(n1-n2) * 6}')
print(f'({n2} - {n2}) / 4 = {(n1-n2) // 4}')
print(f'{n1} // {n2} = {n1 // n2}')
print(f'{n1} / {n2} = {n1 / n2}')
print(f'{n1} % {n2} = {n1 % n2}')
print(f'{n1} * {n2} + 2 = {(n1 * n2) +2 }')
print(f'{n1} ** {n2} = {n1 ** n2}')

print('~'*30)

print(f'Width {width} * Height {height} = {width+height}')

print('~'*30)


#n  # try to access an undefined variable
#Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
#NameError: name 'n' is not defined