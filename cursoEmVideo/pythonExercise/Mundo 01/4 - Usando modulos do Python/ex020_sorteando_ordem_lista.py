# crie um programa que receba o nome de 4 alunos sorteie um nome na lista
#modulo random, metodo choice
import random as r # or from random import choice

al1 = input('Informe o nome do aluno_1: ')
al2 = input('Informe o nome do aluno_2: ')
al3 = input('Informe o nome do aluno_3: ')
al4 = input('Informe o nome do aluno_4: ')
l = [al1, al2, al3, al4]
e = r.choice(l)

print('O aluno escolhido foi {}'. format(e))
