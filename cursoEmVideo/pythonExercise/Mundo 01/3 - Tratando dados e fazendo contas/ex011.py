# crie um programa que leia a largura e a altura de uma parede em metros e calcule sua area e a quantidade de tinta necessaria para pinta-la sabendo que cada litro de tinta pinta uma area de 2m²

altura = float(input('Qual a altura da parede'))
largura = float(input('Qual a largura da parede'))
area = altura * largura
tinta = area / 2

print(
    'Altura: {}m\n'
    'Largura: {}m\n'
    'Area: {}m²\n'
    'Qtd de litros de tinta: {}L'
        .format(altura, largura, area, tinta)
)