# crie um programa que leia um comprimento de tres retas e retorne ao usuario se elas podem ou nao formar um triangulo

print('-=-' * 20)
print('Analisador de triangulos')
print('-=-' * 20 + '\n')
r1 = float(input('Informe a primeira reta em cm: '))
r2 = float(input('Informe a segunda reta em cm: '))
r3 = float(input('Informe a terceira reta em cm: '))

#if (r2 - r3) < r1 < (r2 + r3) and (r1 - r3) < r2 < (r1 + r3) and (r1 - r2) < r3 < (r1 + r3):
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print(f'As retas {r1}cm, {r2}cm e {r3}cm podem formar um triangulo!')
else:
    print(f'As retas {r1}cm, {r2}cm e {r3}cm nao formam um triangulo!')
