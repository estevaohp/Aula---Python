import csv
from pathlib import Path

CAMINHO_CSV = Path(__file__).parent / 'aulaintermediaria15.csv'

lista_clientes = [
    {'Nome':'Estevão Henrique', 'Endereço':'Av 1, 22'},
    {'Nome':'João Henrique', 'Endereço':'Av 2, 22'},
    {'Nome':'Ana Quezia', 'Endereço':'Av 3, 22'},
]

with open(CAMINHO_CSV, 'w') as arquivo:
    nome_colunas = lista_clientes[0].keys()
    escritor = csv.DictWriter(
        arquivo,
        fieldnames=nome_colunas
    )

    for cliente in lista_clientes:
        print(cliente)
        escritor.writerow(cliente)