# crie um programa que leia um numero e  retorne os n primeiros elementos de uma sequencia de fibonacci

print('-' * 30)
print('Sequancia de Fibonacci')
print('-' * 30)
n = int(input('Qauntos termos voce quer mostrar? '))
i = 0
f = 0 #fibonacci[0]
f1 = 1 #fibonacci[1]
f2 = 0 #fibonaci[2]

while i < n:
    f2 = f + f1
    print(f'{f}', end='')
    f = f1
    f1 = f2
    i += 1
    print(' → ' if i < n else ' → Fim!', end='')