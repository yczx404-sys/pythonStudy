s = ord('s')
print(s)
res = list(map(ord, 'spam'))
print(res)
res = [ord(x) for x in 'spam']
print(res)
res = list(map(lambda x : x ** 2, range(10)))
print(res)
res = [x ** 2 for x in range(10)]
print(res)
res = [x for x in range(5) if x % 2 != 1]
print(res)
res = list(filter((lambda x : x % 2 == 0), range(5)))
print(res)

res = [x + y for x in [0, 1, 2] for y in [100, 200, 300]]
tempx = [0, 1, 2]
tempy = [100, 200, 300]
res = [x + tempy[tempx.index(x)] for x in tempx]
res = [tempx[i] + tempy[i] for i in range(len(tempx))]
print(res)

M = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
N = [[2, 2, 2], [3, 3, 3], [4, 4, 4]]
print(M[1])
print(M[1][2])

res = [row[1] for row in M]
print(res)

res = [M[row][1] for row in (0, 1, 2)]
print(res)

res = [M[i][i] for i in range(len(M))]
print(res)

def gensquares(N):
    for i in range(N):
        yield i ** 2
       
for i in gensquares(5):
    print(i, end = ' : ')
    
    
x = gensquares(4)
print(x)
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))  

