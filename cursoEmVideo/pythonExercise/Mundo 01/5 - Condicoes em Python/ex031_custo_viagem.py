# crie um programa que leia a distancia entre 2 pontos em km e calcule o preço da passagem R$ 0.50 por km para viagens < 200km e R$ 0.45 por km para os demais

km = int(input('Informe a distancia entre os dois pontos em km: '))

if km < 200:
    custo = km * 0.50
else:
    custo = km * 0.45

custo1 = km * 0.50 if km <= 200 else km * 0.45
print(f'O custo da viagem é de: R$ {custo}, R$ {custo1}, para a distancia: {km}')