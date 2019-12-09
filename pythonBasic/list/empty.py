class empty:
    def __getattr__(self, attrname):
        if attrname == 'age':
            return 40
        else:
            raise AttributeError(attrname)
    def __setattr__(self, attr, value):
        if attr == 'age':
            self.__dict[attr] = value
        else:
            raise ArithmeticError(attr + 'not allowed')
if __name__ == '__main__':
    X = empty()
    X.age
    X.ane = 'dd'