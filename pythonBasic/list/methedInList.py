# add
l = ['spam', 'st', 'so']
l.append('m')#结果与l + ['m']类似，但是后者会生成新的列表
print(l)
# sort key参数给出了一个单个参数的函数
l.sort(key=str.lower, reverse=True)
print(l)
L=[1, 2]
#list实现先进先出
L.extend([3, 4, 5])
print(L)
L.pop()
print(L)
L.reverse()
print(L)
#注意reversed（）函数与reverse的区别
S = list(reversed(L))
print(S)
print(L)
help(list)
dir(list)