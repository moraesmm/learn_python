# crie um programa que leia uma velocidade de um carro, se ultrapassar 80km/h calcule uma multa de R$ 7 por km acima do limite

v = int(input('Informe a velocidade: '))

if v > 80:
    m = (v - 80) * 7
    print(f'A velocidade maxima é 80kn/h. Sua velocidade foi: {v}, gerando uma multa de R$ {m}, R$ 7 reais por km/h acima do limite.')
else:
    print(f'A velocidade maxima é 80 km/h. Sua velocidade foi {v}!')