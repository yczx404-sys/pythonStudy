import os
# 获取文件的绝对路径
file = 'F:/pythonCode/pythonStudy/padasStudy/oa/record.xlsx'
print(os.path.basename(file)) #返回文件名
print(os.path.dirname(file)) #返回目录路径
print(os.path.split(file)) # 分割文件名和路径， 元组
print(os.path.join('oa','run.txt')) # 文件与路径的合并

print(os.path.getatime(file)) # 获取最近访问时间
print(os.path.getctime(file)) # 获取文件创建时间
print(os.path.getmtime(file)) # 获取文件最近修改时间
print(os.path.getsize(file)) # 获取文件大小
print(os.path.abspath(file)) # 获取文件绝对路径；

print(os.path.exists(file)) # 文件是否存在