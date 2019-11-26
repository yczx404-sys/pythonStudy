import sys
print(sys.path)
#list
print(str([1, 2, 3, 4]) + '34')
#str to list
print(list('43'))
#length
print(len([1, 2, 3]))
# Comcatennation
print([1, 2, 3] + [4, 5, 6])
#Repetition
print(['Ni'] * 4)
#列表迭代与解析
print(3 in [1, 2, 3])
#for 循环
for x in [1, 2, 3]:
    print(x, end=' ')
#列表解析
res = [c * 4 for c in 'sop']
print()
print(res)
#map函数
print(list(map(abs, [-1, -2, 0, 1, 2])))