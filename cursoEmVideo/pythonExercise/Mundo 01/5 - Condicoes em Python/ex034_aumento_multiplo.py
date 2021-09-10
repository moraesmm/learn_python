# crie um programa que leia o slario de um funcionario e retorne o valor do aumento

s = float(input('Informe o valor do salario: '))

if s > 1200:
    s = s * 1.10
else:
    s = s * 1.15

print(f'O novo salrio será: {s}')