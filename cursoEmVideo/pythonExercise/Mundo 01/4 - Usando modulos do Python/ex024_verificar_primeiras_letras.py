# crie um programa que leia o nome de uma cidade e verifica se o inicio do nome = Santo

c = input('Informe o nome da cidade: ')

print('A cidade {} inicia com "{}" e é = a "SANTO"? {}' .format(c, c.upper()[:5], c.upper()[:5] == 'SANTO'))

