# crie um programa que leia um valor em metros e retorne convertido em centimetros e milimetros

m = int(input('Quantos metros?'))

c = m * 100
mi = m * 1000

print(
    'Metros: {}m\n'
    'Centimetros: {}cm\n'
    'Milimetros: {}mm\n'
        .format(m, c, mi))
