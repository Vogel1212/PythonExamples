# course challenge 58
# Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10. 
# Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

from random import randint
comp = randint(0, 10)
print('Hi, Im your computer... I just thought of a number between 0 and 10.')
print('Can you guess which one it was?')
answer = False
guess = 0
while not answer:
    player = int(input('Whats your guess? '))
    guess += 1
    if player == comp:
        answer = True
    else:
        if player < comp:
            print('More... Try again!')
        elif player > comp:
            print('Less... Try again!')
print('Got it right with {} attempts. Congratulations!'.format(guess))
print('Number I thought was {}'.format(comp))