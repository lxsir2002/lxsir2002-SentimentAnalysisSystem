import pandas as pd
import re

# 打开CSV文件
df = pd.read_csv('SentimentClassification/WeiboComments/data/SourceData/weibo_10.csv')

# 提取第列名
header = df.iloc[0]
df = df[1:]

# 去除无效字符
df['review'] = df['review'].apply(lambda x: re.sub(r'[^\w\s]', '', x))

# 规格化标签 0 正面  1 负面
df['label'] = df['label'].map({0: 1, 1: 0})

# 打乱顺序
df = df.sample(frac=1).reset_index(drop=True)

# 计算切分的索引   7 比 3
split_index = int(len(df) * 0.7)

# 分割数据
train_data = df[:split_index]
test_data = df[split_index:]

print(len(train_data))
print(len(test_data))

train_data.to_csv('SentimentClassification/WeiboComments/data/PreData/train_data_10.csv', index=False, columns=["review", "label"])
test_data.to_csv('SentimentClassification/WeiboComments/data/PreData/test_data_10.csv', index=False, columns=["review", "label"])
