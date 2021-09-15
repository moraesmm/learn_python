# crie um programa que leia um numero qualquer e mostre sua factorial

from math import factorial

n = int(input('Digite um numero para calcular seu factorial: '))
c = n
ff = 1

if n > 0:
    f = factorial(n)
    print(f'Calculando {n}! = ', end='')
    while c > 0:
        print(f'{c}', end='')
        print(' x ' if c > 1 else ' = ', end='')
        ff *= c
        c -= 1
    print(f'{f} or {ff}')
elif n == 0:
    print(f'O fatorial de 0 é 1!')
else:
    print('Numero negaivo nao tem numero fatorial!')