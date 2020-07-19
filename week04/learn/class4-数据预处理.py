import numpy as np
import pandas as pd

x = pd.Series([1, 2, np.nan, 3, 4, 5, 6, np.nan, 8])
# 检验序列中是否存在缺陷
x.hasnans

# 将缺失值填充为平均值
x.fillna(value=x.mean())

# DataFrame
df = pd.DataFrame(
    {
        'A':[5, 3, None, 4],
        'B':[None, 2, 4, 3],
        'C':[4, 3, 8, 5],
        'D':[5, 4, 2, None]
    }
)

df.isnull().sum() # 查看缺失值汇总
df.ffill() # 用上一行填充
df.ffill(axis=1) # 用上一列填充

# 缺失值删除
df.info()
df.dropna()

# 填充缺失值
df.fillna('无')

# 重复值处理
df.drop_duplicates()
