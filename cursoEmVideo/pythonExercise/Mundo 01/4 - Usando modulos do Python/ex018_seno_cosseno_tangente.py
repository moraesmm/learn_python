# crie um programa que receba um angulo e retorne o seno, cosseno e tangente

import math as m

ang = float(input('Digite um ângulo: '))
ran = m.radians(ang) # valor convertido em radianos
sen = m.sin(ran)
cos = m.cos(ran)
tan = m.tan(ran)

print(
    'Ângulo: {:.2f}\n'
    'Seno: {:.2f}\n'
    'Cosseno: {:.2f}\n'
    'Tangente: {:.2f}\n'
        .format(ang, sen, cos, tan)
)
