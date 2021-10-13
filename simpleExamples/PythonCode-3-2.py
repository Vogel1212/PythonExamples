# Docs Python
# Usando Python como calculadora, improved version
def calculate():
    operation = input('''
choose an operation:
+ for addition
- for subtraction
* for multiplication
/ for division
''')


    number_1 = int(input('Enter your first number: '))
    number_2 = int(input('Enter your second number: '))

    # Addition
    if operation == '+':
        print('{} + {} = '.format(number_1, number_2))
        print(number_1 + number_2)

    # Subtraction
    elif operation == '-':
        print('{} - {} = '.format(number_1, number_2))
        
        print(number_1 - number_2)

    # Division
    elif operation == '/':
        print('{} / {} = '.format(number_1, number_2))
        print(number_1 / number_2)

    # Multiplication
    elif operation == '*':
        print('{} * {} = '.format(number_1, number_2))
        print(number_1 * number_2)

    #if the operator does not type one of the options provided in the "operation" input, it will display this line
    else:
        print('enter a valid operation please.')

    again()

def again():
    calc_again = input('''
        Want to Calculate again? Yes or No? (Y) or (N)
    ''')

    if calc_again.upper() == 'Y':
        calculate()
    elif calc_again.upper() == 'N':
        print('See you later.')
    else:
        again()

calculate()
