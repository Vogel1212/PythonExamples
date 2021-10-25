# course challenge 14
# Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

temp = float(input('Enter the Temperature in °C: '))
fahr = 1.8*temp+32
print('{}°C Converted to Fahrenheit is {:.1f}°F'.format(temp,fahr))