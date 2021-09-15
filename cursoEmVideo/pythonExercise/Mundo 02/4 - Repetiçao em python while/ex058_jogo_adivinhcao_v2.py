# melhore o desafio 028 onde o computador vai 'pensar' em umnumero entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessarios para vencer

# crie um programa que sorteie um numero e receba um valor do usuario como tentativa de acerto
from random import randint
from time import sleep

c = randint(0, 10) #faz o computador "PENSAR"
s = False #stop
t = 1 #tentativas

print('-=-' * 20)
print('Vou pensar em um número entre 0 e 10. Tente adivinhar...')
print('-=-' * 20 + '\n')

while not s:
    p = int(input('Em que numero eu pensei? '))  # jogada do player1 para tentar adivinhar
    print('Processando...')
    sleep(1)
    if p == c:
        print(f'PARABENS! Voce tentou {t}x e conseguiu adivinhar!')
        s = True
    else:
        print(f'GANHEI! Voce tentou {t}x, eu pensei no numero {c} e nao no {p}!')
        t += 1