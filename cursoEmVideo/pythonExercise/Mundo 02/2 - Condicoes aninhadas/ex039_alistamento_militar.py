# crie um programa que leia a idade e retorne se ele ainda vai se alistar, se é a hora de se alistar ou se já passou do tempo de alistamento

import datetime as dt

a_n = int(input('Informe o ano de nascimento: ')) #ano nascimento
a = dt.date.today().year #ano atual
i = a - a_n #idade
t_f = (18 * 12) - (i * 12) #tempo faltante
t_p = (i * 12) - (18 * 12) #tempo que passou

if i < 18:
    print(f'Ano de nascimento: {a_n}\nidade: {i} em {a}\nainda vai se alistar!\nFaltam(mes): {t_f}')
elif i == 18:
    print(f'Ano de nascimento: {a_n}\nidade: {i} em {a}\né a hora de se alistar!')
else:
    print(f'Ano de nascimento: {a_n}\nidade: {i} em {a}\njá passou do tempo de alistamento!\nPassaram(mes): {t_p}')