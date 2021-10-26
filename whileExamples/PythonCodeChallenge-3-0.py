# course challenge 57
# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça a digitação novamente até ter um valor correto.

#sex = ''
#mess = ''
#while mess != 'Registered information.':
#    sex = str(input('what is your sex [M/F]: ')).upper().strip()
#    if sex == 'M' or sex == 'F':
#        mess = str('Registered information.')
#        print('Registered information.')
#    else:
#        print(end='' 'Invalid option. Try again. ')

# .strip = ignora vários espaços  //  .upper = ignora capslock  //  .upper()[0] = com 0 em colchetes, ele lê apenas o primeiro valor da str

sex = str(input('what is your sex [M/F]: ')).strip().upper()[0]
while sex not in 'MmFf':
    sex = str(input('Invalid data. Please enter your gender: ')).strip().upper()[0]
print('Gender {} successfully registered'.format(sex))
        
        