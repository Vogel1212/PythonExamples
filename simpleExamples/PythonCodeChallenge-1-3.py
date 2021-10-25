#course challenge 6
#Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

nota1 = float(input('enter the first note: \n'))
nota2 = float(input('enter the second note: \n'))
media = (nota1 + nota2) / 2

# {:.1f} = depois do ponto flutuante coloque apenas um digito
print('The average between {:.1f} e {:.1f} its the same as: {:.1f}'.format(nota1,nota2,media))

if media < 6:
    print("You Fail, Study for Recovery!!")
else: 
    print("Congratulations, You're Approved!")

