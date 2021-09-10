# crie um programa que leia tres numeros e retorne o maior e o menor

n1 = int(input('Informe um numero: '))
n2 = int(input('Informe um numero: '))
n3 = int(input('Informe um numero: '))
l = [n1, n2, n3]

print(
    f'Min(): {min(l)}\n'
    f'Max(): {max(l)}\n')

if n1 > n2 and n1 > n3:
    print(f'Max: {n1}')
else:
    if n2 > n1 and n2 > n3:
        print(f'Max: {n2}')
    else:
        print(f'Max: {n3}')

if n1 < n2 and n1 < n3:
    print(f'Min: {n1}')
else:
    if n2 < n1 and n2 < n3:
        print(f'Min: {n2}')
    else:
        print(f'Min: {n3}')
