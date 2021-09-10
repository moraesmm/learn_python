# crie um programa para aprovar um emprestimo bancario para compra de uma casa. O programa deve receber o valor da casa, slario e tempo para pagamento da divida.
#Calcule o valor da prestaçao mensal sabendo que ela nao pode exceder 30% do slario

cores = {'limpa':'\033[m',
        'verde':'\033[1;32m',
        'azul':'\033[1;34m',
        'vermelho':'\033[1;31m',
        'amarelo': '\033[33m'}

comprador = str(input('Bom dia!\nPor favor, me informe seu nome: ')).upper()
casa = float(input(f'Qual o valor da casa {comprador}? R$'))
salario = float(input(f'Qual seu salrio {comprador}? R$'))
t_pagamento = int(input('Quantas parcelas {}mensais{}? '. format(cores['amarelo'], cores['limpa'])))
parcela_max = salario * 0.30
casa_mensal = casa / t_pagamento

if casa_mensal > parcela_max:
    print(
        '\n{}Nao podemos comprar essa casa!{}\n'
        'Valor da casa: R${}\n'
        'Valor do slario: R${}\n'
        'Tempo de pagamento(mes): {}\n'
        'Valor de parcela maxima: R${}{}{} -> ({} * 30%)\n'
        'Valor da parcela simulada: R${}{:.2f}{} -> ({} / {})'
            . format(
                cores['vermelho'], cores['limpa'],
                casa,
                salario,
                t_pagamento,
                cores['vermelho'] , parcela_max, cores['limpa'], salario,
                cores['vermelho'], casa_mensal, cores['limpa'], casa, t_pagamento))
else:
    print(
        '\n{}Podemos comprar essa casa!{}\n'
        'Valor da casa: R${}\n'
        'Valor do slario: R${}\n'
        'Tempo de pagamento(mes): {}\n'
        'Valor de parcela maxima: R${}{}{} -> ({} * 30%)\n'
        'Valor da parcela simulada: R${}{:.2f}{} -> ({} / {})'
            .format(
            cores['verde'], cores['limpa'],
            casa,
            salario,
            t_pagamento,
            cores['verde'], parcela_max, cores['limpa'], salario,
            cores['verde'], casa_mensal, cores['limpa'], casa, t_pagamento))