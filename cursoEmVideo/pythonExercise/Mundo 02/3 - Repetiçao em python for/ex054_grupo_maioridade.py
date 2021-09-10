# crie um programa que leia o ano de nascimento de sete pessoas e retorne quantas pessoas atingiram a maior idade e quantas nao atingiram
from datetime import date as dt

maior_idade = ''
menor_idade = ''
maior_idade_qtd = 0
menor_idade_qtd = 0

for count in range(0, 7):
    n = str(input('Informe seu nome: '))
    i = int(input('Informe seu ano de nascimento: '))

    if dt.today().year - i >= 18:
        maior_idade = maior_idade + n + ':' + str(i) + '\n'
        maior_idade_qtd += 1
    else:
        menor_idade = menor_idade + n + ':' + str(i) + ' com ' + str(dt.today().year - i) + ' anos\n'
        menor_idade_qtd += 1

print(f'Lista de pessoas maior de idade (>=18 anos), tem {maior_idade_qtd} pessoas:\n{maior_idade}\n'
      f'Lista de pessoas menor de idade (<18 anos), tem {menor_idade_qtd} pessoas:\n{menor_idade}')

