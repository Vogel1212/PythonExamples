#course challenge 6
#Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

nota1 = float(input('Digite a primeira nota: \n'))
nota2 = float(input('Digite a segunda nota: \n'))
media = (nota1 + nota2) / 2

# {:.1f} = depois do ponto flutuante coloque apenas um digito
print('A média entre {:.1f} e {:.1f} é igual a: {:.1f}'.format(nota1,nota2,media))

if media < 6:
    print("Você está Reprovado, Estude para a Recuperação!!")
else: 
    print("Parabéns, Você está Aprovado!")

