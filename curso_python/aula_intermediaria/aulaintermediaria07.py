from datetime import datetime
from pytz import timezone

data = datetime.now()
print(data.timestamp)

# data = datetime.now(timezone('Asia/Tokio'))
# print(data)
# # data_str_data = '2024/12/02 08:52:04'
# # data_str_fmt = '%Y/%m/%d %H:%M:%Y'

# # data = datetime.strptime(data_str_data,data_str_fmt)
# # print(data)
# # # data = datetime(2024, 12, 2, 8,43,12)
# # # print(data)

