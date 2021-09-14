# refaça o ex051, leia o primeiro termo e a razao de um PA, retorne os 10 primeiros termos da progressao

n = int(input('Digite o primeiro termo da PA: ')) #primeiro termo
r = int(input('Digite a razao da PA: ')) #razao
d = n + (10 - 1) * r #decimo

while n < d + r:
    print(f'{n}')
    n += r
