# crie um programa que leia o nome de uma pessoa e retorne se o nome dela contem SILVA

nome = input('Digite o nome: ')

print('O nome {} contem "SILVA"? {}'
        .format(nome, 'SILVA' in nome.upper()))
        #.format(nome, (nome.upper().find('SILVA') > 0)))