# transforma valor int em float
num1 = float(input('Enter an integer value: '))
print(num1)

# apresenta valores boleanos
num2 = bool(input('Enter an even value for True and no value for False: '))
print(num2)

# True para numero e False para str
num3 = input('type something: ')
print(num3.isnumeric())

# False para numero e True para str
num4 = input('type something: ')
print(num4.isalpha())

# é ou não alfa numérico
num5 = input('type something: ')
print(num5.isalnum())