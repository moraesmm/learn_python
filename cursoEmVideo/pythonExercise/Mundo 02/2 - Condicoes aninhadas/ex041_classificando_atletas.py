# crie um programa que laia o ano de nascimento de um atleta e retorne a categoria <=9: mirim, <=14: infantil, <=19: junior, <=20: senior ou master

from datetime import date as dt

a = int(input('Informe o ano de nascimento: '))
i = dt.today().year - a

if i <= 9:
    print('Voce está na categoria: Mirim')
elif i <= 14:
    print('Voce está na categoria: Infantil')
elif i <= 19:
    print('Voce está na categoria: Junior')
elif i <= 20:
    print('Voce está na categoria: Senior')
else:
    print('Voce está na categoria: Master')