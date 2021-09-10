# crie um programa que leia um numero e retorne se ele é impar ou par

n = int(input('Informe um numero: '))
r = n % 2

if r == 0:
    print(f'O numero: {n} é par!')
else:
    print(f'O numero: {n} é impar!')