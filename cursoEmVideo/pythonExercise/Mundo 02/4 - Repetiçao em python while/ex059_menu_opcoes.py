# crie um programa que leia dois valores e mostre um menu na tela [1]Somar, [2]Multiplicar, [3]Maior, [4]Novos numeros, [5]Sair do programa

print('-=-' * 20)
print('Vamos utilizar 2 numeros e fazer algumas operaçoes')
print('-=-' * 20 + '\n')
n1 = float(input('Digite o primeiro numero: '))
n2 = float(input('Digite o segundo numero: '))
s = False #stop

while not s:
    print('-=-' * 20)
    print('[1] somar')
    print('[2] multiplicar')
    print('[3] maior')
    print('[4] novos numeros')
    print('[5] sair do programa')
    p = int(input())
    print('-=-' * 20 + '\n')

    # operacoes
    if p == 1: #soma
        print(f'A soma de {n1} e {n2} é: {n1 + n2}')
    elif p == 2: #multiplicar
        print(f'A multiplicação de {n1} e {n2} é: {n1 * n2}')
    elif p == 3: #maior
        if n1 == n2:
            print(f'O numero {n1} e {n2} sao iguais!')
        elif n1 > n2:
            m = n1
            print(f'O maior entre {n1} e {n2} é: {n1}')
        else:
            m = n2
            print(f'O maior entre {n1} e {n2} é: {n2}')
    elif p == 4: #novos numeros
        s = False
        n1 = float(input('Digite o primeiro numero: '))
        n2 = float(input('Digite o segundo numero: '))
    elif p == 5: #sair
        s = True
    else:
        print('Numero invalido!')

print('Fim!')