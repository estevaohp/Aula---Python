##forma simples

def duplicar(numero):
    return numero * 2
print(duplicar(4))

def triplicar(numero):
    return numero * 3
print(triplicar(2))

def quadruplicar(numero):
    return numero * 4
print(triplicar(2))


##forma mais complexa

def criar_multiplicador(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
