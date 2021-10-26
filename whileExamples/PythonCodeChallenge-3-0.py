# course challenge 57
# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça a digitação novamente até ter um valor correto.

sex = ''
mess = ''
while mess != 'Informação registrada.':
    sex = str(input('Qual seu sexo [M/F]: ')).upper().strip()
    if sex == 'M' or sex == 'F':
        mess = str('Informação registrada.')
        print('Informação registrada.')
    else:
        print(end='' 'Opção inválida. Tente novamente. ')
        
        
        