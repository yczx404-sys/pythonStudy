#列表分片会返回一个新的对象
L = ['spam', 'SPAM', 'spam!']
print(L)
print(L[-2])
print(L[0:2])#半开半闭
#列表的更新
L[1] = 'eggs'
print(L)
L[0 : 2] = ['eat', 'more']
print(L)
#分片赋值的本质操作是先删除这个分片然后在添加
L=['a', 'b', 'c', 'd', 'e', 'f']
L[1:3] = ['g']
print(L)