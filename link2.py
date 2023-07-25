# 1905060103 辛天宇

import pandas as pd

data = pd.read_csv(r'C:\Users\86131\Desktop\测试数据爬取\fyx_chinamoney.csv')
code_list = data['112282672'].tolist()

batch_size = 80
num_batches = len(code_list) // batch_size + (1 if len(code_list) % batch_size != 0 else 0)
for i in range(num_batches):
    start_index = i * batch_size
    end_index = min((i + 1) * batch_size, len(code_list))
    batch = code_list[start_index:end_index]
    print(batch)
