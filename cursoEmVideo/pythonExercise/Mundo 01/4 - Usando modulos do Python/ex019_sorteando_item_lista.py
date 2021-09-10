# crie um programa que receba o nome de 4 alunos sorteie e sorteie a ordem de apresentacao
# modulo: random >> metodo shuffle
import random as r # or from random import shuffle

al1 = input('Informe o nome do aluno: ')
al2 = input('Informe o nome do aluno: ')
al3 = input('Informe o nome do aluno: ')
al4 = input('Informe o nome do aluno: ')
l = [al1, al2, al3, al4]
e = r.shuffle(l)

#print('A ordem de apresentaçao será {}'. format(e))
print('A ordem de apresentaçao será {}')
print(l)



