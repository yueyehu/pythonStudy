# -*- coding: cp936 -*-
'''比较Python自带的数学运算与numpy中的运算的效率'''
import time
import math
import numpy as np
x = [i*0.001 for i in xrange(1000000)]
start = time.clock()
for i,t in enumerate(x):
    x[i] = math.sin(t)
print "math.sin:",time.clock() - start

x = [i*0.001 for i in xrange(1000000)]
x = np.array(x)
start = time.clock()
np.sin(x,x)
print "numpy.sin:",time.clock() - start

x = [i*0.001 for i in xrange(1000000)]
start = time.clock()
for i,t in enumerate(x):
    x[i] = np.sin(t)
print "numpy.sin loop:",time.clock() - start


