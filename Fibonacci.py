# -*- coding: cp936 -*-
'''�������޸�Fibonacii����'''
def fib():
    '''Fibonacci�����޽�������'''
    x,y = 0,1
    while True:
        yield x
        x,y = y,x+y
if __name__ == "__main__":
    import itertools
    print list(itertools.islice(fib(),10))
