# crie um programa que leia o preço normal e condiçao de pagamento e retone o valor de venda
# ['à vista dinheiro/ cheque':'10% desconto'
# ['à vista no cartao':'5% desconto'
# ['em até 2x no cartao':'0% desconto'
# ['3x ou mais no cartao':'20% juros'

p = float(input('Informe o preço normal: R$')) #preço normal
c = input(
            'Informe a condiçao de pagamento (1, 2, 3 ou 4):\n'
            '1 -> À vista no dinheiro ou cheque\n'
            '2 -> À vista no cartao\n'
            '3 -> Em até 2x no cartao\n'
            '4 -> 3x ou mais no cartao\n') #condicao de pagamento

if int(c) == 1:
    c = 'À vista no dinheiro ou cheque'
    p_final = p * 0.9
elif int(c) == 2:
    c = 'À vista no cartao'
    p_final = p * 0.95
elif int(c) == 3:
    c = 'Em até 2x no cartao'
    p_final = p
elif int(c) == 4:
    parcela = int(input('Quantas parcelas? '))
    p_final = p * parcela * 1.2
    print(f'O preço: R${p}\nem {parcela} parcelas\nvalor final: R${p_final:.2f}')
    exit()
else:
    print('Numero invalido!')
    exit()

print(f'O preço: R${p}\nforma de pagamento: {c}\nvalor final: R${p_final:.2f}')