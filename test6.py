import time
N = 40000000
'''
start = time.time()
for i in xrange(N):pass
print "xrange:",time.time()-start

start = time.time()
for i in range(N):pass
print "range:",time.time()-start

start = time.time()
for i in xrange(N):pass
print "xrange:",time.time()-start
'''

import itertools
def frange(start,end=None,inc=1.0):
    if end == None:
        end = start + 0.0
        start = 0.0
    assert inc 
    for i in itertools.count():
        next = start + i*inc
        if (inc > 0.0 and next>=end) or (inc < 0.0 and next<=end):
            break
        yield next

import math
def frange1(start,end=None,inc=1.0):
    if end == None:
        end = start + 0.0
        start = 0.0
    nitems = int(math.ceil((end - start)/inc))
    for i in xrange(nitems):
        yield start + i*inc

import math,numpy
def frange2(start,end = None,inc=1.0):
    if end == None:
        end = start + 0.0
        start = 0.0
    nitems = int(math.ceil((end - start)/inc))
    return numpy.arange(nitems)*inc + start

start = time.time()
f = frange(N)
print "frange:",time.time()-start

start = time.time()
f = frange1(N)
print "frange1:",time.time()-start

start = time.time()
f = frange2(N)
print "frange1:",time.time()-start
        
