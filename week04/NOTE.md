学习笔记
# 字符串和整数之间的装换
    ord('a')
    chr(97)
# pandas
## pandas基础数据类型
### Series
### 1.创建Series
```python
import pandas as pd

# 创建Serier对象
# 1.通过字典创建
data = {'a':1, 'b':2, 'c':3}
s1 = pd.Series(data)
print(s1)

# 2.通过列表创建
s2 = pd.Series([1,2,3], index=['a','b','c'])
print(s2)

# a    1
# b    2
# c    3
# dtype: int64
```
### 2.Series的属性
```python
print(s1.index, type(s1.index))
# >>> Index(['a', 'b', 'c'], dtype='object') <class 'pandas.core.indexes.base.Index'>
print(s1.values, type(s1.values))
# >>> [1 2 3] <class 'numpy.ndarray'>

# ndarray数据类型转为pandas的数据类型列表
l1 = s1.values.tolist()

# >>> [1, 2, 3]
```
### 3.Series查找数据
```python
# 行号查找
print(s1[:2])
# >>> a    1
# >>> b    2
# >>> dtype: int64

# 索引查找
print(s1[['a', 'c']])
# >>> a    1
# >>> c    3
# >>> dtype: int64

# Series的map方法获取bool值序列，筛选数据

print(s1.map(lambda x: x > 2))
print(s1[s1.map(lambda x: x > 2)])

# >>> a    False
# >>> b    False
# >>> c     True
# >>> dtype: bool
# >>> c    3
# >>> dtype: int64

eamil = pd.Series(['abc at amzom.com','admin1235.com', 'itcast@163.com'])

import re
pattern = '[A-Za-z0-9_.] + @[A-Za-z0-9._] + \.[A-Za-z]{2,5}'
mask = email.map(lambda x:bool(re.match(pattern,x)))
print(email[mask])

# 使用index会提升查询性能
#   如果index唯一，pandas会使用哈希表优化，查询性能为0(1)
#   如果index有序不唯一， pandas会使用二分法算法，查询性能为0(logN)
#   如果index完全随机，则每次查询都要扫描表，查询性能为0(n)
```
### DataFrame
```python
# 创建DataFrame对象
```

# 数据预处理