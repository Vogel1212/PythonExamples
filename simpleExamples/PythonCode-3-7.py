from datetime import date

nome = input(('Qual é seu nome?'))

def calculaIdade(birthDate):
    days_in_year = 365.2425    
    age = int((date.today() - birthDate).days / days_in_year) 
    return age 

print(calculaIdade("Certificamos que", nome,", ",date(12/10/1999)), "anos, ", "Foi aceito no curso gratuito de programção")

#não completo