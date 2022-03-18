quantm = cont = maior = 0
man_name = ''
for c in range(1, 5):
    print(f'--- {c}ª pessoa ---')
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    cont += idade
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F]')).strip().upper()[0]
        if c == 1 and sexo == 'M':
            maior = idade
            man_name = nome
    if sexo == 'M' and idade > maior:
        man_name = nome
    if sexo == 'F' and idade < 20:
        quantm += 1
media = cont / 4

print(f'A média de idade do grupo é {media}')
print(f'O nome do homem mais velho é {man_name}')
print(f'{quantm} tem menos de 20 anos')
