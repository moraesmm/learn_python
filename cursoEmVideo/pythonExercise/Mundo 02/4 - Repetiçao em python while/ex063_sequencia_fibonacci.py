# crie um programa que leia um numero e  retorne os n primeiros elementos de uma sequencia de fibonacci

n = int(input('Digite a quantidade de elementos que voce gostaria de exibir da sequencia Fibonacci: '))
i = 0
f = 0 #fibonacci[0]
f1 = 1 #fibonacci[1]
f2 = 0 #fibonaci[2]

while i < n:
    f2 = f + f1
    print(f'{f}')
    f = f1
    f1 = f2
    i += 1