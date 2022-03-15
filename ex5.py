print('-='*20)
print(f'{"AUMENTO SALÁRIAL":^35}')
print('-='*20)
salario = float(input('Seu salário atual: '))
news = 0
if salario > 1250:
    news = salario + (salario * 10 / 100)
else:
    news = salario + (salario * 15 / 100)
print(f'O seu salario era de {salario} após o aumento passa a ser {news}')

