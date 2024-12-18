def zipper (l1, l2):
    intervalo_maximo = min(len(l1), len(l2))
    return[(l1[i], l2[i]) for i in range(intervalo_maximo)]
    


l1 = ["Salvador", "Ubatuba", "Belo Horizonte"]
l2 = ["BA", "SP", "MG", "RJ"]
print(zipper(l1, l2))
 