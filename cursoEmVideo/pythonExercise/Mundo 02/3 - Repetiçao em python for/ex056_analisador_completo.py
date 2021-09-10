# crie um programa que leia o nome, idade e sexo de 4 pessoas e retorne a media de idade do grupo, o nome do homem mais velho e quantas mulheres tem menos de 20 anos

i_soma = 0 #soma das idades
i_media = 0 #idade media
i_velho = 0 #idade homem mais velho
n_velho = '' #nome homem mais velho
qtd_mulher = 0 #quantidade de mulheres < 20 anos

for count in range(0,4):
    #inputs
    print(f'\n------- {count + 1} PESSOA -------')
    n = str(input('Digite o nome: '))
    i = int(input('Digite a idade: '))
    s = str(input('Digite o sexo(M/F): ')).upper()

    # calculation
    i_soma += i                        #soma das idades digitadas para criar media
    if s == 'M' and i > i_velho:        #se sexo = m e idade digitada > idade do mais velho
        i_velho = i                         #idade mais velho atualizada para idade digitada
        n_velho = n                         #nome mais velho atualizado para nome digitado
    if s == 'F' and i < 20:             #se sexo = f e idade digitada menor que 20
        qtd_mulher += + 1                   #quantidade de mulher abaixo dos 20 anos atualizado para valor atual +1

i_media = i_soma / 4               #idade media do grupo (soma das idades/ quantidade de pessoas)

    #return
print(
    f'\nA media de idade do grupo é {i_media:.2f}\n'
    f'O homem mais velho tem {i_velho} e se chama {n_velho}\n'
    f'Ao todo sao {qtd_mulher} mulheres com menos de 20 anos')



