# -*- coding: cp936 -*-
class Book(object):
    '''python中创建属性的实验'''
    def __setattr__(self, name, value):        
        if name == 'value':
            self.k = name
            object.__setattr__(self, name, value - 50)
        else:
            object.__setattr__(self, name, value)
    def __getattr__(self, name):
        try:
            return object.__getattribute__(name)
        except:
            return name + ' is not found!'
    def __str__(self):
        return self.name + ' cost : ' + str(self.value)
c = Book()
print c
c.name = 'Python'
c.value = 100
c.new = 50
print c.k
print c.name
print c.value
print c.new
print c
print c.Type
