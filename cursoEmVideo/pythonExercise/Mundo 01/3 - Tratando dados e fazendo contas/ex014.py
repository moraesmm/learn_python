# crie um programa que leia a temperatura em °C e converta para °F

c = float(input('Informe a temperatura em °C'))
f = (9 * c) /5 +32

print(
    'Temperatura {}°C\n'
    'Temperatura {:.2f}°F'
        .format(c, f))