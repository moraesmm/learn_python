# crie um porgrama que leia o nome completo de uma pessoa e retorne o nome com todas as letras maiuscula, todas as letras minuscula, quantidade de letras sem contar o espaço, quantas letras tem no primeiro nome

nome = input('Digite seu nome completo: ')
u_nome = nome.upper()
l_nome = nome.lower()
#nome_sem_espaco = nome.replace(' ', '')
#len_nome = len(nome_sem_espaco)
len_nome = len(nome.replace(' ', ''))
#len_primeiro_nome = nome.split()
#qtd_letras = len(len_primeiro_nome[0])
qtd_letras = len(nome.split()[0])
nome_fisrt = nome.split()[0]

print(
    'Nome completo: {}\n'
    'Nome maiusculo: {}\n'
    'Nome minusculo: {}\n'
    'Nome tamanho : {}\n'
    'Quantidade letras em {}: {}'
        .format(nome, u_nome, l_nome, len_nome, nome_fisrt, qtd_letras)
)