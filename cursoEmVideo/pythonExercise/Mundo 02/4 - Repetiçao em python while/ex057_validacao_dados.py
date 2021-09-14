# crie um programa que leia o sexo de uma pessoa e só aceite M ou F, caso esteja errado peça a digitaçao novamente ate ter um valor valido

r = ''

while r not in ('F', 'M'):
    r = str(input('Digite seu sexo [F/M]: ')).upper()
    if r not in ('F', 'M'):
        print('Formato invalido, informe o sexo no formato [F/M]!')

if r == 'F':
    print('Olá Sra!')
else:
    print('Olá Sr!')