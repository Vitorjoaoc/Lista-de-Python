from ex10.lib.interface import *
from ex10.lib.arquivo import *
from time import sleep

arq = 'cadastropessoas.txt'
if not arquivoExiste(arq):
    criarArquivo(arq)


while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova Pessoa', 'Sair do Sistema'])
    if resposta == 1:
        #opção de listar o conteúdo de um arquivo
        lerArquivo(arq)
    elif resposta == 2:
       #opção de cadastrar uma nova pessoa
        cabeçalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabeçalho('Saindo do sistema... Até logo!')
        break
    else:
        print('\033[0;31mERRO! Digite uma opção válida!\033[m')
    sleep(2)



