import numpy as np
import pandas as pd
date1=pd.date_range("20190114", periods=6)
df=pd.DataFrame(np.arange(2,26).reshape(6,4),index=date1,columns=['a','b','c','d']);
print(df)
#行下标和列下标确定一个唯一的值
print(df.loc['2019-01-15','b'])

#第一行
print(df.loc['2019-01-15'])

#通过索引
print('-------------------------')
#第一行
print(df.iloc[0:3,[0,1]])
print('-------------------------')
#通过索引和下标(不建议使用)
print(df.ix[0:3,['a','b']])
#条件选择
# df代表范围.a代表'a'列ki
print(df[df.a>8])
print(df[df['b']==11])
print(df[(df.a==10)&(df.c==12)])
#行操作
#前3行，默认5行A
print(df.head(3))
print(df.tail(2))

print(df['b'])
#添加一行
data={'a':49,'b':34,'c':12,'d':98}
s = pd.Series(data)
s.name='2019-02-21'
df=df.append(s)
print(df)


