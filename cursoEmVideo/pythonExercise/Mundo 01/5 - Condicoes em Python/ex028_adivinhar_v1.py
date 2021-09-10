# crie um programa que sorteie um numero e receba um valor do usuario como tentativa de acerto
"""
# minha criaçao
import random as r

t = int(input('Digite um numero de 1 a 5: '))
l = [0,1,2,3,4,5]
if t == int(r.choice(l)):
    print(f'Voce acertou no sorteio numero digitado: {t} numero sorteado: {r.choice(l)}')
else:
    print(f'Voce errou, o numero sorteado era: {r.choice(l)}')
"""

from random import randint
from time import sleep

c = randint(0, 5) # faz o computador "PENSAR"
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20 + '\n')
p = int(input('Em que numero eu pensei? ')) # jogador tenta adivinhar
print('Processando...')
sleep(1)

if p == c:
    print('PARABENS! Voce conseguiu adivinhar!')
else:
    print(f'GANHEI! Eu pensei no numero {c} e nao no {p}!')