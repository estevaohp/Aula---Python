from time import sleep
from threading import Thread

class MeuTheread(Thread):
    def __init__(self, texto, tempo):
        self.texto = texto
        self.tempo = tempo

        super().__init__()

    def run(self):
        sleep(self.tempo)
        print(self.texto)

t1 = MeuTheread('Theread 1', 2)
t1.start()

t2 = MeuTheread('Theread 2', 3)
t2.start()

t3 = MeuTheread('Theread 3', 4)
t3.start()

for i in range(20):
    print(i)
    sleep(1)