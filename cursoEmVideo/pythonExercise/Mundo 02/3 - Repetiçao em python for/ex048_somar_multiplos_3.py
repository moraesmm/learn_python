# crie um programa que calcule a soma entre os numeros impares que sao multiplos de 3 de 1 até 500

s = 0
qtd = 0

for i in range(1, 501, 2):
    if i % 3 == 0:
        s += i
        qtd += 1
        print(f'{qtd} -> {i} + {s} = {s + i}')

print(f'São: {qtd} valores e a soma: {s}')