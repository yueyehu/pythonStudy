class _const(object):
    class ConstError(TypeError):pass
    def __setattr__(self,name,value):
        if name in self.__dict__: 
            raise self.ConstError, "can't rebind const (%s)"%name
        self.__dict__[name] = value
    def __delattr__(self,name):
        if name in self.__dict__:
            raise self.ConstError, "can't unbind const (%s)"%name
        raise NameError, name
    class __metaclass__(type):
        def __setattr__(self,name,value):
            print "haha"

class _const1():
    class ConstError(TypeError):pass
    def __setattr__(self,name,value):
        #if name in self.__dict__: 
         #   raise self.ConstError, "can't rebind const (%s)"%name
        self.__dict__[name] = value
    def __delattr__(self,name):
        if name in self.__dict__:
            raise self.ConstError, "can't unbind const (%s)"%name
        raise NameError, name
import sys
sys.modules[__name__] = _const() 
