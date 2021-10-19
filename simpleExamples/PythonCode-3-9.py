# transforma valor int em float
num1 = float(input('Digite um valor inteiro: '))
print(num1)

# apresenta valores boleanos
num2 = bool(input('Digite um valor par para True e nenhum valor para False: '))
print(num2)

# True para numero e False para str
num3 = input('Digite algo: ')
print(num3.isnumeric())

# False para numero e True para str
num4 = input('Digite algo: ')
print(num4.isalpha())

# é ou não alfa numérico
num5 = input('Digite algo: ')
print(num5.isalnum())