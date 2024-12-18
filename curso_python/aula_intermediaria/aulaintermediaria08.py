from datetime import datetime

fmt = '%d/%m/%Y %H:%M:%S'
data_inicio = datetime.strptime('02/12/1997 09:30:09', fmt)
data_fim = datetime.strptime('02/12/2024 09:30:09', fmt)
print(data_fim - data_inicio)
# print(data_fim > data_inicio)
# print(data_fim < data_inicio)
