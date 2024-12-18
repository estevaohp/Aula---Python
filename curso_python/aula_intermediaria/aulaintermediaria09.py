from datetime import datetime

fmt = '%d/%m/%Y'
# data = datetime(2024, 12, 2, 9, 38, 4)
data = datetime.strptime('2024-12-02 09:41:53', '%Y-%m-%d %H:%M:%S')
print(type(data.strftime(fmt)))
print(data.strftime(fmt))