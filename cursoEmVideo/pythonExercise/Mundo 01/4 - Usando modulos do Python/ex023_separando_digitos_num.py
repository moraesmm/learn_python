# crie um programa que leia um numero de 0 a 9999 e retorne cada um dos digitos separados

num = int(input('Digite um numero de 0 a 9999? '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

print(
    'Numero: {}\n'
    'Unidade: {}\n'
    'Dezena: {}\n'
    'Centena: {}\n'
    'Milhar: {}'
        .format(num, u, d, c, m))
        #.format(num, num[3], num[2], num[1], num[0])) #if type(num) == str