# crie um programa que leia o nome completo de uma pessoa e retorne o primeiro e o ultimo nome separadamente

n = input('Digite um nome completo: ')
n_first = n.split()[0]
n_last = n.split()[n.count(' ')]

print(
    'O nome: {}\n'
    'Primeiro nome: {}\n'
    'Ultimo nome: {}'
        .format(n.title(), n_first.title(), n_last.title()))
