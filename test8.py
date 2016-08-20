'''cook book 20.1'''
def make_adder(addend):
    def adder(augend):
        return addend+augend
    adder.__name__ = 'add_%s'%(addend,)
    return adder

plus100 = make_adder(100)
plus23  = make_adder(23)

print plus100(1000),plus23(1000)
print plus100,plus23

'''cook book 20.2'''
class C(object):
    def __init__(self):
        self._x = None

    def getx(self):
        return self._x

    def setx(self,value):
        self._x = value

    def delx(self):
        del self._x
    x = property(getx,setx,delx,"I'm the 'x' property")

class Parrot(object):
    def __init__(self):
        self._voltage = 1000

    @property
    def voltage(self):
        '''Get the current voltage.'''
        return self._voltage

class D(object):
    def __init__(self):
        self._x = None
    @property
    def x(self):
        '''I'm the 'xxx' property.'''
        return self._x

    @x.setter
    def x(self,value):
        self._x = value

    @x.deleter
    def x(self):
        del self._x

import math
class Rectangle(object):
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def area():
        doc = "Area of the Rectangle"
        def fget(self):
            return self.x*self.y
        def fset(self,value):
            ratio = math.sqrt((1.0*value)/self.area)
            self.x *= ratio
            self.y *= ratio
        return locals()
    area = property(**area())

def sss(v):
    '''sss:decorator'''
    print "This is a Decorator"
    return v*v

def ss(v):
    v()
    return sss
@ss
def s():
    print "This is a Decorator"
    pass
