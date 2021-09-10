# crie um programa que leia dois numeros inteiros e retorne se o primeiro valor é o maior ou se o segundo valor é o maior ou se sao iguais

n1 = int(input('Informe um numero: '))
n2 = int(input('Informe outro numero: '))

if n1 > n2:
    print(f'O primeiro valor é o maior {n1}!')
elif n2 > n1:
    print(f'O segundo valor é o maior {n2}!')
else:
    print('Os numeros sao iguais!')