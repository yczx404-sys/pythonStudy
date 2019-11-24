import pandas as pd
import numpy as np
#创建series利用numpy
s=pd.Series(np.arange(1,6))
print(s)
print("--------------------")
#第二种方法，传入类表
s=pd.Series([1,2,3,6,np.nan,44])
print(s)
print("---------------")
#增加行标签
s=pd.Series([1,2,3,6,np.nan,44], index=['a','b','c','d','e','f'])
print(s)
print('------------')
print(s.index)
print(s.values)
print(s[0])
print(s[1:4])
