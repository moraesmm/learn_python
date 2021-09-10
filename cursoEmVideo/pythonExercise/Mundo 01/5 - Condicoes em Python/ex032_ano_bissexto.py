# crie um programa que leia um ano e retorne se ele é um ano bissexto

ano = int(input('Informe um ano: '))

if ano % 4 == 0:
    print(f'O ano {ano} é bissexto!')
else:
    print(f'O ano {ano} não é bissexto!')