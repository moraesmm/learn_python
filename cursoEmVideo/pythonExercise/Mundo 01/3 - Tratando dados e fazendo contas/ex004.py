# crie um programa que leia algo pelo teclado e retorne o seu tipo primitivo e todas as informaçoes possiveis sobre ele

msg = input('Digite aqui uma mensagem')

print(
    'O tipo primitivo desse valor é: {0}\n'
    'Msg é um alfanumerico? {1}\n'
    'Msg é um alfabeto? {2}\n'
    'Msg é um numero? {3}\n'
    'Msg é um decimal? {4}\n'
    'Msg é minusculo? {5}\n'
    'Msg é maiusculo? {6}'
    .format(
        type(msg),
        msg.isalnum(),
        msg.isalpha(),
        msg.isnumeric(),
        msg.isdecimal(),
        msg.islower(),
        msg.isupper()))

