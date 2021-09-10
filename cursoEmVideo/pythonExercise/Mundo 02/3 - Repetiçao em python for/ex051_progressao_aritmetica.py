# desenvolva um programa que leia um primeiro termo e a razao de uma PA e retorne os 10 primeiros termos dessa progressao

n = int(input('Digite o primeiro termo da PA: ')) #primeiro termo
r = int(input('Digite a razao da PA: ')) #razao
d = n + (10 - 1) * r #decimo
i = 1

for i in range(n, d + r, r):
    #print(f'a{i} = {n} + ({i} - 1) * {r}')
    print(f'{i} ')