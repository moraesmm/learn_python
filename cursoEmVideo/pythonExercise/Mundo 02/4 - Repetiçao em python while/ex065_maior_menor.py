# crie um programa que leia varios numeros, retorne a media, o maior e o menor o usuario deve informar quando parar
s = 0 #stop
n_menor = 0 #menor numero
n_maior = 0 #maior numero
n_soma = 0 #soma dos numeros
n_media = 0 #media do numero
n_qt = 0 #quantidade de numeros

while s == 0:
    n = int(input('Digite um valor: '))
    n_qt += 1
    n_soma += n
    s = int(input('Digite 1 se quiser parar, digite 0 se quiser continuar.'))

    if n_qt == 1: #o primeiro numero informado sempre será o menor e o maior valor da lista
        n_menor = n
        n_maior = n

    if n > n_maior:
        n_maior = n
    elif n < n_menor:
        n_menor = n

n_media = n_soma / n_qt
print(
    f'\nMaior numero: {n_maior}\n'
    f'Menor numero: {n_menor}\n'
    f'Quantidade de numeros: {n_qt}\n'
    f'Soma dos numeros: {n_soma}\n'
    f'Media dos numeros: {n_media:.2f}\n')