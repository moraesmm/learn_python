# crie um programa que leia o salario e retorne um novo valor com 15% de aumento

s = float(input('Informe o salario'))

print(
    'Salario: {}\n'
    'Salario com aumento: {}'
        .format(s,s * 1.15)
)