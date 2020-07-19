import pandas as pd

# 创建Serier对象
# 1.通过字典创建
data = {'a':1, 'b':2, 'c':3}
s1 = pd.Series(data)
print(s1)
# 2.通过列表创建
s2 = pd.Series([1,2,3], index=['a','b','c'])
print(s2)


# index和values
print(s1.index, type(s1.index))
print(s1.values, type(s1.values))

l1 = s1.values.tolist()
print(l1)

# 行号查找
# print(s1[:2])
# #
# print(s1[['a', 'c']])
# Series的map方法获取bool值列表，筛选数据

print(s1.map(lambda x: x > 2))
print(s1[s1.map(lambda x: x > 2)])

email = pd.Series(['abc at amzom.com','admin1235.com', 'itcast@163.com', 'amin1@15.com'])

import re
pattern = '[A-Za-z0-9_.]+@[A-Za-z0-9._]+\\.[A-Za-z]{2,5}'
mask = email.map(lambda x:bool(re.match(pattern,x)))
print(mask)
print(email[mask])


# DataFrame
import pandas as pd
import numpy as np
# 1.创建DataFrame对象
## 1.1 通过字典数据创建

data = {
    '武汉':
}
df = pd.DataFrame()