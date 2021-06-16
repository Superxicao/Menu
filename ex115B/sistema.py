from lib.interface import *
from lib.arquivo import *
from time import sleep

arq='pessoas.txt'
#if not arquivoExiste(arq):
 #   print('')

while True:
    resposta=menu(['Ver Pesoas Cadastradas','Cadastrar Pessoas','Sair do Sistema'])
    if resposta==1:
        print('')
    elif resposta==2:
        print('')
    elif resposta==3:
        print('')
    else:
        print('Erro, {} não é uma opção válida.'.format(resposta))
    sleep(2)