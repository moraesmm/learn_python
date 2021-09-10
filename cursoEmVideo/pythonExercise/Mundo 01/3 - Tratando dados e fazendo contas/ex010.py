# crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostra a conversao para dolares

reais = float(input('Quantos reais voce tem na carteira'))

print(
    'Reias: R$ {}\n'
    'Dolar: U$ {:.2f}'
        .format(reais,reais/3.27))

