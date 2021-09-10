# crie um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo e calcule e retorne o comprimento da hipotenuza

import math as m

co = float(input('Informe o comprimento do cateto oposto: '))
ca = float(input('Informe o comprimento do cateto adjacente: '))
h = (co ** 2 + ca ** 2) ** 0.5
hi = m.hypot(co, ca)

print(
    'Cateto oposto: {}\n'
    'Cateto adjacente: {}\n'
    'Hipotenusa: {:.2f}\n'
    'Math.Hipotenusa: {:.2f}'
        .format(co, ca, h, hi))