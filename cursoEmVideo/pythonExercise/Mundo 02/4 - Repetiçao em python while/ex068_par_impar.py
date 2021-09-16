# crie um programa que jogue par ou impar até o jogador perder, retorne quantas vitorias o jogador teve
import random as r

s = False #stop
e_jogador = '' #escolha do jogador
n_partida = 0

while s == False:
    e_jogador = ''
    n_jogador = 0
    n_computador = 0

    print('-' * 20)
    print('Vamos jogar par ou impar!')
    print('-' * 20)

    while e_jogador not in ('PAR', 'IMPAR', 'P', 'I'):
        e_jogador = str(input('Voce gostaria de escolher [par/ impar]: ')).upper()
        if e_jogador not in ('PAR', 'IMPAR', 'P', 'I'):
            print(f'Digite um valor valido [PAR, IMPAR, P, I]')

    n_jogador = int(input('Digite seu numero: '))
    n_computador = r.randint(0, 10)
    n_soma = n_jogador + n_computador

    if n_soma % 2 == 0:
        if e_jogador in ('PAR', 'P'):
            print(f'Voce ganhou, a soma de {n_jogador} + {n_computador} é {(n_jogador + n_computador)} que é par!')
            n_partida += 1
        else:
            print(f'Voce PERDEU!')
            break
    else:
        if e_jogador in ('IMPAR', 'I'):
            print(f'Voce ganhou, a soma de {n_jogador} + {n_computador} é {(n_jogador + n_computador)} que é par!')
            n_partida += 1
        else:
            print(f'Voce PERDEU!')
            break

print('-' * 20)
print(f'Voce venceu {n_partida}x!')
print('-' * 20)