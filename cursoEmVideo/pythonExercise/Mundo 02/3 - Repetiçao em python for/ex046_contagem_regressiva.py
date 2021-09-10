# crie um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artificio, indo de 10 até 0 com pausa de 1 segundo

import time as t
i = 0

for i in range(i, 10):
    print(f'Falta {10 - i} segundos para estourar os fogos!')
    print('####' * (i + 1))
    t.sleep(1)

print('-=-=-=-=-=-=-=-= BOOOOM =-=-=-=-=-=-=-=-')