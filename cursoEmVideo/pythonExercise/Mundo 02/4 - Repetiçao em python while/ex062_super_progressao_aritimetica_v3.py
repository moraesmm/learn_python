# refaça o ex062, leia o primeiro termo e a razao de um PA, retorne os 10 primeiros termos da progressao
# pergunte se o usuario gostaria de ver mais termos

n = int(input('Digite o primeiro termo da PA: ')) #primeiro termo
r = int(input('Digite a razao da PA: ')) #razao
rr = 10 #rerun
d = n + rr * r #decimo

while n < d + r:
    while n < d + r:
        print(f'{n}')
        n += r
    rr = int(input('Digite a quantidade de termos a mais voce gostaria de visualizar: '))
    if rr > 0:
        d = n + rr * r  # decimo