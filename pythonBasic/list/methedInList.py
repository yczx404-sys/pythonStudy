# add
l = ['spam', 'st', 'so']
l.append('m')#结果与l + ['m']类似，但是后者会生成新的列表
print(l)
# sort key参数给出了一个单个参数的函数
l.sort(key=str.lower, reverse=True)
print(l)
