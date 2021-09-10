# Leia um numero e retorne o sobro, triplo e raiz quadrada

n1 = int(input('Digite um valor'))

d = n1 * 2
t = n1 * 3
r = n1 ** 0.5  # or pow(n1,0.5)

print('Valor digitado {}, dobro {}, triplo {} e raiz quadrada {:.2f}!' .format(n1, d, t, r))
