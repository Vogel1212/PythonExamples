# course challenge 14
# Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

temp = float(input('Digite a Temperatura em °C: '))
fahr = 1.8*temp+32
print('{}°C Convertido para Fahrenheit é {:.1f}°F'.format(temp,fahr))