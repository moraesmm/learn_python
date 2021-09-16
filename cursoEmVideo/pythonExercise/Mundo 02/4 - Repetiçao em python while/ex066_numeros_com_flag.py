# crie um programa que leia varios numeros, o programa deve parar quando o usuario digitar 999. Retorne a quantidade de numeros digitados e a soma entre eles

n = 0
n_qt = 0
n_soma = 0

while n != 999:
    n = int(input('Digite um numero [999 para parar]: '))
    if n != 999:
        n_qt += 1
        n_soma += n
    else:
        break

print(f'Voce digitou {n_qt} numeros e a soma foi {n_soma}')