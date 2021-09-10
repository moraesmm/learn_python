# crie um programa que leia a quantidade de km percorrido por um carro alugado e a quantidade de dias que o carro foi alugado

d = int(input('Informe os dias: '))
km = float(input('Informe os km: '))

custo_dia = 60
custo_km = 0.15
custo_dia_total = d * custo_dia
custo_km_total = km * custo_km
custo_total = custo_dia_total + custo_km_total

print(
    'Quantidade de dias: {}\n'
    'Quantidade de km: {}\n'
    'Custo por dia R$: {:.2f}\n'
    'Custo por km R$: {:.2f}\n'
    'Custo total por dia R$: {:.2f}\n'
    'Custo total por km R$: {:.2f}\n'
    'Custo total R$: {:.2f}'
        .format(d, km, custo_dia, custo_km, custo_dia_total, custo_km_total, custo_total))