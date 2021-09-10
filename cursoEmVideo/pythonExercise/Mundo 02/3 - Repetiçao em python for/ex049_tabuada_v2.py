# crefaça o ex009, mostrando a tabuada de um numero que o usuario digitar utilizando laço for
# ex009 crie um programa que leia um numero inteiro e retorne sua tabuada

i = 1
n = int(input('Digite um valor: '))

for i in range(i, 11):
    print(f'{n} x {i} = {n * i}')