# crie um programa que leia o peso e a altura de uma pessoa e retorne seu IMC <18.5:abaixo do peso, <25:peso ideal, <30:sobrepeso, <40:obesidade e obesidade morbida

p = float(input('Informe o peso: ')) #peso
a = float(input('Informe a altura: ')) #altura
IMC = p / (a ** 2) #peso/(altura*altura)

if IMC < 18.5:
    print(f'O peso: {p} está abaixo do ideal, IMC: {IMC:.2f} , resultado: peso abaixo!')
elif IMC < 25:
    print(f'O peso: {p} está dentro do ideal, IMC: {IMC:.2f} , resultado: peso ideal!')
elif IMC < 30:
    print(f'O peso: {p} está no sobrepeso, IMC: {IMC:.2f} , resultado: sobrepeso!')
elif IMC < 40:
    print(f'O peso: {p} está obeso, IMC: {IMC:.2f} , resultado: obeso!')
else:
    print(f'O peso: {p} está obeso morbido, IMC: {IMC:.2f} , resultado: obesidade morbida!')