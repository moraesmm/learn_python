# crie um programa que leia uma frase e retorne quantas vezes aparece "A" em que posicao ela aparece pela primeira vez em que posicao ela aparece a ultima vez

f = str(input('Digite uma frase: ')).upper().strip()

c = str(input(('Qual letra vc deseja procurar: '))).upper()
f_count = f.count(c)
f_find = f.find(c) + 1
f_last = f.rfind(c) + 1

print('A frase {}\n'
      'Len da frase: {}\n'
      'Contem a letra {} {}x\n'
      'A primeira vez que a letra "{}" apareceu foi na posicao: {}\n'
      'A ultima vez que a letra "{}" apareceu foi na posicao: {}\n'
        .format(f, len(f), c, f_count, c, f_find, c, f_last))