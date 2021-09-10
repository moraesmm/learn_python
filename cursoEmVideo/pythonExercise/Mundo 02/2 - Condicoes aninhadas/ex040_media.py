# crie um programa que leia duas notas de um aluno e calcule sua media mostrando uma msg no final, m < 5 REPROVADO, M < 7 RECUPERACAO e 7 > = APROVADO

cores = {'limpa':'\033[m',
        'verde':'\033[1;32m',
        'azul':'\033[1;34m',
        'vermelho':'\033[1;31m',
        'amarelo': '\033[33m'}

n1 = float(input('Digite uma nota: '))
n2 = float(input('Digite outra nota: '))
m = (n1 + n2) / 2


if m < 5:
    print('Sua media foi {:.1f}, voce foi {}REPROVADO{}!! '. format(m, cores['vermelho'], cores['limpa']))
elif m < 7:
    print('Sua media foi {:.1f}, voce está de {}RECUPERACAO{}!! '.format(m, cores['amarelo'], cores['limpa']))
else:
    print('Sua media foi {:.1f}, voce foi {}APROVADO{}!! '.format(m, cores['verde'], cores['limpa']))