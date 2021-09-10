# crie um programa que leia um numero e retorne se ele é primo ou nao

cores = {'limpa':'\033[m',
        'verde':'\033[1;32m',
        'azul':'\033[1;34m',
        'vermelho':'\033[1;31m',
        'amarelo': '\033[33m'}

n = int(input('Digite um numero: '))
mult = 0 #quantidade de multiplos

for count in range(1, n + 1): #todo numero primo é maior que 1
    if (n % count == 0):
        print('{}Multiplo de: {}{}' .format(cores['verde'], count, cores['limpa']))
        mult += 1
    else:
        print('{} Não é multiplo de: {}{}' .format(cores['vermelho'], count, cores['limpa']))

print('\n')
print('-=-' * 10)
#print('Resultado: ')

if mult == 2:
    print('{}Numero primo!{}' .format(cores['verde'], cores['limpa']))
else:
    print('{}Tem {} multiplos <= {}{}' .format(cores['vermelho'], mult, n, cores['limpa']))

print('-=-' * 10)