import pandas as pd
import numpy as np
#https://www.cnblogs.com/-wenli/p/10271475.html
#传入二位数组创建
date1=pd.date_range("20190114",periods=6)
print(date1)
#生成6行4列,index为行标签，columns为lie标签
df=pd.DataFrame(np.random.randn(6,4),index=date1,columns=['a','b','c','d'])
print(df)
#使用字典
df1= pd.DataFrame({'A':1,
                   'B':pd.Timestamp('20190114'),
                   'C':np.array([3]*4, dtype='int32'),
                   'E':pd.Categorical(['test','train','test','train']),
                   'F':'foo',
                   'G':pd.Series([1,2,3,4])})
print(df1)

print(df1.dtypes)#查看每列的类型
print(df1.index)#查看行下标
print(df1.columns)#查看列下标
print(df1.values)#查看所有
print(df1.describe())#查看平均数，方差