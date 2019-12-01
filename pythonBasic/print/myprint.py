print()
x = 'spam'
y = 99
z = ['eggs']
print(x, y, z)
print(x, y, z, sep='')
print(x, y, z, sep=",")
print(x, y, z, sep='...', file=open('data.txt', 'w'))
print([line for line in open('data.txt')])

pi = 3.1415926
# 字段宽10， 精度3
print('%10.3f' % pi)
# * 表示从后面元组中读取精度
print('pi = %.*f' % (3, pi))
# 用0填充空白
print('%010.3f' % pi)
# 左对齐
print('%-10.3f' % pi)
#显示正负号
print('%+f' % pi)
def add(*numbers):
    print(numbers)
    sum = 0
    for i in numbers:
        sum += i
    return sum
a1 = (1, 2, 3, 4, 5, 6)
# print(add(a1))
print(add(*a1))
a2 = [1, 2, 3, 4]
print(add(*a2))
#print(add(a2))

