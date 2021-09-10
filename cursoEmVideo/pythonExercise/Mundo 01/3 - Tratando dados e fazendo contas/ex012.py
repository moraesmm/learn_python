# crie um programa que leia um preço e retorne um novo valor com 5% de desconto

p = float(input('Informe o preço'))

print(
    'Preço: {}\n'
    'Preço com desconto: {:.2f}'
        .format(p,p * 0.95)
)