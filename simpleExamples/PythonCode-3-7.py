from datetime import date

nome = input(('Whats your name?'))

def calculaIdade(birthDate):
    days_in_year = 365.2425    
    age = int((date.today() - birthDate).days / days_in_year) 
    return age 

print(calculaIdade("we certify that", nome,", ",date(12/10/1999)), "years, ", "Was accepted into the free programming course")

#não completo