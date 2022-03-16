from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''Suas opções:
[0] Pedra
[1] Papel
[2] Tesoura''')
jogador = int(input('Qual é a sua jogada?' ))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
while jogador > 2 or jogador< 0:
    print('JOGADA INVÁLIDA!')
    print('''Suas opções:
    [0] Pedra
    [1] Papel
    [2] Tesoura''')
    jogador = int(input('Qual é a sua jogada?'))
print('-=' * 13)
print(f'O computador jogou {itens[computador]}')
print(f'O jogador jogou {itens[jogador]}')
print('-=' * 13)
if computador == 0: #pedra
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCE')
    elif jogador == 2:
        print('COMPUTADOR VENCE')

elif computador == 1: #papel
    if jogador == 0:
        print('COMPUTADOR VENCE')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR VENCE')

elif computador == 2:  #tesoura
    if jogador == 0:
        print('JOGADOR VENCE')
    elif jogador == 1:
        print('COMPUTADOR VENCE')
    elif jogador == 2:
        print('EMPATE')


