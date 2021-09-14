# crie um programa que leia um numero qualquer e mostre sua factorial

n1 = int(input('Digite um numero: '))
n = 1
f = 0

if n1 > 0:
    while n1 != n:
        print(f'{f} + ({n1} x {n}) = {f + (n1 * n)}')
        f = f + (n1 * n)
        n += 1
    print(f'O fatorial de {n1} é {f}!')
elif n1 == 0:
    print(f'O fatorial de 0 é 1!')
else:
    print('Numero negaivo nao tem numero fatorial!')