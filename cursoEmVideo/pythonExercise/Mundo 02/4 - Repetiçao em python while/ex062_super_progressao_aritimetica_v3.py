# refaça o ex062, leia o primeiro termo e a razao de um PA, retorne os 10 primeiros termos da progressao
# pergunte se o usuario gostaria de ver mais termos

n = int(input('Digite o primeiro termo da PA: ')) #primeiro termo
n_qt = 0 #quantidade de termos
r = int(input('Digite a razao da PA: ')) #razao
rr = 9 #rerun
d = n + rr * r #decimo

while n < d + r:
    while n < d + r:
        print(f'{n}', end='')
        n += r
        n_qt += 1
        print(' → ' if n < d + r else ' → PAUSA!', end='')

    rr = int(input('\nQuantos termos voce quer mostrar a mais? '))
    if rr > 0:
        d = n + (rr - 1) * r  # decimo

print(f'Progressao finalizada com {n_qt} termos!')