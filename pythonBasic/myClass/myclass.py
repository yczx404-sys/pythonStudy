class MixedNames:
    data = 'spam'
    def __init__(self, value):
        self.data = value
    def display(self):
        print(self.data, MixedNames.data)
class NextClass:
    def printer(self, text):
        self.message = text
        print(self.message)
class Super:
    def method(self):
        print('in super method')
    
    def delegate(self):
        raise NotImplementedError('action must be defined')
class Inheritor(Super):
    pass
class Replacer(Super):
    def method(self):
        print('in Replacer.method')
class Extender(Super):
    def method(self):
        print('startting Extender.method')
        Super.method(self)
        print('ending Extender.method')
class Provider(Super):
     def action(self):
         print('in Provider.action')
class Sub(Super):
    def method(self):
        print('startting sub.method')
        Super.method(self)
        print('ending Sub.method')
       
if __name__ == '__main__':
   #x = MixedNames(1)
   #y = MixedNames(2)
   #x = NextClass()
   #NextClass.printer(x, 'hello world')
   #print(x.message)
   #x = Super()
   #x.method()

   #x.method()
   x = Super()
   print(x.delegate())