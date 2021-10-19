#course challenge 4
#Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possiveis sobre ele.

num1 = input('Digite algo: ')
print('O tipo primitivo desse valor é ', type(num1))
print('Todos os caracteres na string são alfanuméricos?:',num1.isalnum())
print('True se todos os caracteres na string estão no alfabeto:',num1.isalpha())
print('True se todos os caracteres forem ascii: ',num1.isascii())
print('True se todos os caracteres na string forem decimais:',num1.isdecimal())
print('True se todos caracteres forem digitos:',num1.isdigit())
print('True se a str é um identificador:',num1.isidentifier())
print('True se todos caracteres forem numeros:',num1.isnumeric())
print('True se todos caracteres forem imprimiveis:',num1.isprintable())
print('True se todos os caracteres forem espaços em branco:',num1.isspace())
print('True se a string segue as regras de um titulo:',num1.istitle())
print('True se todos os caracteres são maíusculos:',num1.isupper())
