# crie um programa que leia uma frase e retorne se ela é um palindromo desconsiderando os espcaços

f = str(input('Digite uma frase: ')).replace(' ', '')
f_contraio = ''

for count in range(len(f), 0, -1):
    f_contraio = f_contraio + f[count-1]

if f == f_contraio:
    print(f'A frase: "{f}" é um palíndromo! {f_contraio}')
else:
    print(f'A frase: "{f}" não é um palíndromo! {f_contraio}')