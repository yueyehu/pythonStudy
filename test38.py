def factorial_v3(n=5):
 
    return n and factorial_v3(n-1)*n or 1

              
def factorial_v4(n=5):
 
    f = lambda n: reduce(lambda a,b:a*b ,xrange(2,n+1))
 
    return f(n)
