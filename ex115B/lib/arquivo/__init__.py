#ex115B>lib>arquivo>__init__.py

from ex115B.lib.interface import *

#a = open(nome, 'rt', encoding='utf-8')
def arquivoExiste(nome):
    try:
        a=open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True
    
def criarArquivo(nome):
    try:
        a=open(nome,'wt+')
        a.close()
    except:
        print('Houve um erro.')

def lerArquivos(nome):
    try:
        a=open(nome,'rt')
    except:
        print('Erro ao ler o arquivo')
    else:
        cabecalho('Pessoas Cadastradas')
        print(a.readlines())
