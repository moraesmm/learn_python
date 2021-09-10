# crie um programa que leia a escolha do usuario para o jogo pedra, pepel ou tesoura e e retone uma escolha aleatoria e o resultado do jogo

import random as r
from time import sleep as s

print('-=-' * 20)
print('Vamos jogar!')
print('-=-' * 20 + '\n')
j = input(
            'Escolha uma opçao (1, 2 ou 3):\n'
            '1 -> Pedra\n'
            '2 -> Papel\n'
            '3 -> Tesoura\n')
c = r.choice(['Pedra', 'Papel', 'Tesoura']) #or c = r.randint(1, 3)

if int(j) == 1:
    j = 'Pedra'
    if c == 'Tesoura':
        r = 'ganhou'
    elif c == 'Pedra':
        r = 'empatou'
    else:
        r = 'perdeu'
elif int(j) == 2:
    j = 'Papel'
    if c == 'Pedra':
        r = 'ganhou'
    elif c == 'Papel':
        r = 'empatou'
    else:
        r = 'perdeu'
elif int(j) == 3:
    j = 'Tesoura'
    if c == 'Papel':
        r = 'ganhou'
    elif c == 'Tesoura':
        r = 'empatou'
    else:
        r = 'perdeu'
else:
    print('Numero invalido!')
    exit()

print('JO')
s(1)
print('KEN')
s(1)
print('PO!!')
s(0.5)
print('-=' * 20)
print(f'Voce {r}!\nSua escolha: {j}!\nEscolha do computador: {c}!')
print('-=' * 20)