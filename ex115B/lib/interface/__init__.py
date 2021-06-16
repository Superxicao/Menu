#ex115B>lib>interface>__init__.py

def linha(tam=42):
    return '-'*tam

def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())

def leiaint(msg):
    while True:
        try:
            n=int(input(msg))
        except:
            print('Erro, digite um número válido.')
            continue
        else:
            return n

def menu(lista):
    cabecalho('MENU PRINCIPAL')
    c=1
    for item in lista:
        print(f'{c} - {item}')
        c+=1
    print(linha())
    opc=leiaint('Sua opção: ')
    return opc