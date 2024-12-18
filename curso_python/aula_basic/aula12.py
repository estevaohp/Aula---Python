class Camera:
    def __init__(self, nome, filmando = False):
         self.nome = nome
         self.filmando = filmando 

    def filmar(self):
         if self.filmando:
              print(f'{self.nome} Já está filmando...')
              return
         
         print(f'{self.nome} está filmando...')
         self.filmando = True

    def fotogragar(self):
         if self.filmando:
              print(f'{self.nome} não pode fotografar filmando...')
              return
         


c1= Camera ('Canon')
c1= Camera ('Sony')
c1.filmar()
c2.filamr()
    