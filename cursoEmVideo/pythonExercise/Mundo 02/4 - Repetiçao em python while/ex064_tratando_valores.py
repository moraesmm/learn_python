# crie um programa que leia varios numeros, o programa deve parar quando o usuario digitar 999, retorne a quantidade de numeros digitados e a soma entre eles

r = 0 #resposta do usuario
q_n = 0 #quantidade de numeros digitados
s_n = 0 #soma dos numeros digitados

n = float(input('Digite um numero [999 para sair]: '))

while n != 999:
    q_n += 1
    s_n += n
    n = float(input('Digite um numero [999 para sair]: '))

print(f'Voce digitou {q_n} numeros e a soma foi {s_n:.1f}!')