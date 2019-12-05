counters = [1, 2, 3, 4]
def inc(x): 
    return x + 10
res = list(map(inc, counters))
print(res)
print(list(map((lambda x : x + 3), counters)))