# crie um programa que leia duas notas de um aluno, calcule e mostre sua media

n1 = int(input('Digite a primeira nota'))
n2 = int(input('Digite a segunda nota'))

m = (n1 + n2) /2

print(
    'Nota 1: {}\n'
    'Nota 2: {}\n'
    'Média: {}'
        .format(n1, n2, m))
