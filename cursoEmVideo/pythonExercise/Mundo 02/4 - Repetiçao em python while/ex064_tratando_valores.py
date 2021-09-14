# crie um programa que leia varios numeros, o programa deve parar quando o usuario digitar 999, retorne a quantidade de numeros digitados e a soma entre eles

r = 0 #resposta do usuario
q_n = 0 #quantidade de numeros digitados
s_n = 0 #soma dos numeros digitados

while r != 999:
    n = float(input('Digite um numero: '))
    q_n += 1
    s_n += n
    r = int(input('Digite 999 para sair ou qualquer numero para continuar!'))

print(f'Voce digitou {q_n} numeros e a soma foi {s_n:.1f}!')