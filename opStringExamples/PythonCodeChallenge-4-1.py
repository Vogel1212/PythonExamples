# course challenge 24
# Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO".

city = str(input('What city were you born in? ')).strip()
print(city[:5].upper() == 'SANTO')