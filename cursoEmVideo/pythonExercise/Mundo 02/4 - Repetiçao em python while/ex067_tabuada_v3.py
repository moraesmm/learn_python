# refaça o ex0049, o programa só devera ser interrompido quando o usuario digitar um numero negativo

n = 0

while n >= 0:
    n = int(input('Digite um valor: '))
    i = 1
    if n > 0:
        for i in range(i, 11):
            print(f'{n} x {i} = {n * i}')