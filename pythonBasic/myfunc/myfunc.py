import sys
counters = [1, 2, 3, 4]
def inc(x): 
    return x + 10
print(list(map(inc, counters))
#showall = (lambda x : list(map(sys.stdout.write, x)))
#t = showall(['spam\n', 'toast\n'])
#showall2 = lambda x : [sys.stdout.write(line) for line in x]
#t = showall2(('bright\n', 'side\n'))
#def action(x):
#    return (lambda y : x + y)
#act = action(99)
#print(act)
#print(act(2))
#
#
#
#
#if __name__ == '__main__':
    #f = lambda x, y, z : x + y + z
    #print(f(2, 3, 4))
    #x = (lambda a = 'fee', b = 'fie', c = 'foe' : a + b + c)
    #print(x('wee'))
    #def knigths():
    #    title = 'Sir'
    #    action = (lambda x : title + " " + x)
    #    return action
    #act = knigths()
    #print(act('robin'))
    #
    #L = [lambda x : x ** 2, lambda x : x ** 3, lambda x : x ** 4]
    #for f in L : 
    #    print(f(2))
    #print(L[0](3))
    #lowers = (lambda x, y : x if x < y else y)
    #print(lowers('bb', 'aa'))
    #print(lowers('aa', "bb"))
    