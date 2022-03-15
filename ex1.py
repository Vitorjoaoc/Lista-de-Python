from math import sqrt
while True:
    n1 = int(input('Digite um número: '))
    print(f'O dobro de {n1} é {n1 * 2} e seu triplo é {n1 * 3}')
    print(f'A raiz quadrada de {n1} é {sqrt(n1)}')
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if resp == 'N':
        break
print('<< OBRIGADO VOLTE SEMPRE >>')



