# crie um programa que leia um numero em seguida leia a opçao de conversao (1 - binario, 2 - octal, 3 - hexadecimal)

n = int(input('Informe um numero: '))
c = int(input('Informe qual conversão deseja fazer (1, 2 ou 3): \n1 -> Binario\n2 -> Octal\n3 -> Hexadecimal\n'))

if c == 1:
    r = bin(n)
    c = 'binario'
elif c == 2:
    r = oct(n)
    c = 'octal'
elif c == 3:
    r = hex(n)
    c = 'hexadecimal'
else:
    print('Numero invalido!')
    exit()

print(f'A conversao do numero inteiro {n} para {c} é: {r}!')