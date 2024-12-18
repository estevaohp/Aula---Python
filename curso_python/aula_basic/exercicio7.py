def soma(x,y):
    return x + y

def multiplica(x,y):
    return x * y

def executa(funcao, *args):
    def interna(*args):
     return funcao(*args)
    return interna


soma_com_cinco = criar_funcao(soma, 5)
multiplica_por_dez = criar_funcao(multiplica, 10)

print(soma_com_cinco(10))
print(multiplica_por_dez(10))