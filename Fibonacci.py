# -*- coding: cp936 -*-
'''生成无限个Fibonacii数列'''
def fib():
    '''Fibonacci数的无界生成器'''
    x,y = 0,1
    while True:
        yield x
        x,y = y,x+y
if __name__ == "__main__":
    import itertools
    print list(itertools.islice(fib(),10))
