import enum 

class Direcoes(enum.Enum):
    ESQUERDA = 1
    DIREITA = 2


def mover(direcao: Direcoes):
    if not isinstance(direcao, Direcoes):
        raise ValueError('Direção não encontrada')
    
    

    print(f'Movendo para {direcao.name}({direcao.value})')


mover(Direcoes.ESQUERDA)
mover(Direcoes.DIREITA)
