# crie um programa que leia a idade e o sexo, a cada pessoa o programa devera perguntar se o usuario gostria de continuar a adicionar pessoas. O programa deve retornar quantas pessoas > 18 anos, quantos homens e quantas mulheres < 20 anos

c = ''
i_18 = 0
qt_h = 0
qt_m = 0

while c != 'N':
    c = ''
    i = int(input('Digite a idade: '))
    s = str(input('Digite o sexo [M/ F]: ')).upper()

    if s in ('M'):
        qt_h += 1

    if i > 18:
        i_18 += 1

    if s in ('F') and i < 20:
        qt_m += 1

    while c not in ('S', 'N'):
        c = str(input('Voce gostaria de continuar [S/ N]? ')).upper()

    if c == 'N':
        break

print(f'\n> 18 anos: {i_18}\n'
      f'Quantidade de homens: {qt_h}\n'
      f'Quantidade de mulheres < 20 anos: {qt_m}')