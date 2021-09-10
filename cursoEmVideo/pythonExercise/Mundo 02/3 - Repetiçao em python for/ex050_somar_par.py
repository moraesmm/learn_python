# crie um programa que leia 6 numeros e calcule a soma somente dos os numeros pares

i = 0
s = 0
qtd = 0

for i in range(i, 6):
    n = int(input('Digite um numero: '))
    if n % 2 == 0:
        print(f'{s} + {n} = {s + n}')
        s += n
        qtd += 1

print(f'Voce informou {qtd} numeros pares e a soma foi {s}')