print('ALUGUEL DE CARROS')
print('-='*10)
dias = int(input('Por quantos dias alugou o carro? '))
km = float(input('Quantos KM foram percorridos? '))
valor = (dias * 60) + (km * 0.15)
print(f'Você alugou o carro por {dias} dias e percorreu {km}km o valor total a pagar ficou em  R&{valor}')

