import pandas as pd
import numpy as np
# 通过list创建series对象
s = pd.Series([1, 3, 5, np.nan, 6, 8])
print(s)
# 创建dataFrame
dates = pd.date_range("20130101", periods=6)
print(dates)

df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))
print(df)

# 通过传递类似结构的字典创建DataFrame
df2 = pd.DataFrame({'A':1, 
                    'B': pd.Timestamp('20130102'),
                    'C': pd.Series(1, index=list(range(4))),
                    'D': np.array([3] * 4, dtype='int32'),
                    'E': pd.Categorical(['test', 'train', 'test', 'train']),
                    'F': 'foo'})
print(df2)

# from ndarray to create Series
s = pd.Series(np.random.randn(5), index=['a','b','b','d','e'])
print(s)
print(s.index)
g = pd.Series(np.random.randn(5))
print(s)
print(s.index)
# create Series from dict
d = {'b':1, 'a' : 0, 'c' : 2}
s = pd.Series(d)
print(s)
d = {'a' : 0, 'b' : 1, 'c': 2}
s = pd.Series(d)
print(s)
s = pd.Series(d, index=['b', 'c', 'd', 'a'])
print(s)

s = pd.Series(5., index=['a', 'b', 'c'])
print(s)
print(g[g > g.median()])
print(np.exp(s))
print(g.dtype)
print(s.array)
s = pd.Series(np.random.randn(5), index=['a','b','b','d','e'])
print(s['a'])
print(s)
print('f' in s)
print('e' in s)