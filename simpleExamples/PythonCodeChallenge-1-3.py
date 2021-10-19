#course challenge 6
#Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

nota1 = int(input('Digite a primeira nota: \n'))
nota2 = int(input('Digite a segunda nota: \n'))
media = nota1 + nota2 / 2

print('A sua média é {}'.format(media))

if media <= 6:
    print("Você está Reprovado!")
#elif media >= 7:
#    print("Você está Aprovado!")
else: 
    print("Você está Aprovado!")

