from time import sleep
print('-=' * 10)
print(f'{"TABUADA":^20}')
print('-=' * 10)
resp = ' '
while resp not in 'N':
    n = int(input('Você quer saber a tabuada de qual número? '))
    print('Imprimindo...')
    sleep(2)
    cont = 1
    while cont <= 10:
        print(f'{n} x {cont} = {n * cont}')
        cont += 1
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]')).strip().upper()[0]
        if resp == 'N':
            break
print('<< VOLTE SEMPRE >>')