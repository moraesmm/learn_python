# crie um programa que leia um numero real qualquer e retorne sua porçao inteira
import math as m
# from math import trunc

n = float(input('Digite um numero '))
i = m.trunc(n)

print(
    'Numero digitado: {}\n'
    'Numero inteiro: {}'
        .format(n, i))