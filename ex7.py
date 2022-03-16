from time import sleep
from random import randint
cont = 0
print('-='*20)
print(f'{"JOGO DE ADVINHAÇÃO":^35}')
print('-='*20)
print('Vou sortear em um número entre 1 e 20 tente advinhar!')
computador = randint(1, 20)
print('Sorteando...')
sleep(2)
while True:
    jogador = int(input('Qual foi o número sorteado? '))
    if jogador > computador:
        print('\033[0;31mVOCÊ PERDEU!\033[m Tente novamente um número menor.')
        cont += 1
    elif jogador < computador:
        print('\033[0;31mVOCÊ PERDEU!\033[m Tente novamente um número maior.')
        cont += 1
    else:
        print(f'\033[0;32mVOCÊ GANHOU!\033[m')
        break
print(f'Parabéns, você precisou de {cont} tentativa(s) para ganhar.')








