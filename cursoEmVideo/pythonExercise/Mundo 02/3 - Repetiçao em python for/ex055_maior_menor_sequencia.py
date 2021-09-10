# crie um programa que leia o peso de 5 pessoas e retorne o maior e menor peso

p_list = []

for count in range(0, 5):
    p = float(input('Digite o peso: '))
    p_list.append(p)

print(f'A pesso mais pesada foi {max(p_list)}kg e a pessoa mais leve foi {min(p_list)}kg!')


# resoluçao do video do curso

maior = 0
menor = 0

for count in range(0, 5): #faça a mesma açao 5 vezes count = (0, 1, 2, 3, 4)
    p = float(input('Digite o peso: '))
    if p == 0: #o primeiro peso informado sempre será o menor e o maior valor da lista
        maior = p
        menor = p
    else:
        if p > maior:
            maior = p
        if p < menor:
            menor = p

print((f'O maior peso foi {maior} e o menor foi {menor}!'))
