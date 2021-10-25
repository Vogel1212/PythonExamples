#course challenge 4
#Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possiveis sobre ele.

num1 = input('Type something: ')
print('The primitive type of this value is ', type(num1))
print('Are all characters in the string alphanumeric?:',num1.isalnum())
print('True if all characters in string are in alphabet:',num1.isalpha())
print('True if all characters are ascii: ',num1.isascii())
print('True if all characters in string are decimal:',num1.isdecimal())
print('True if all characters are typed:',num1.isdigit())
print('True if str is an identifier:',num1.isidentifier())
print('True if all characters are numbers:',num1.isnumeric())
print('True if all characters are printable:',num1.isprintable())
print('True if all characters are blanks:',num1.isspace())
print('True if the string follows the rules of a title:',num1.istitle())
print('True if all characters are uppercase:',num1.isupper())
