def func(data):
    count = [data]
    def wrap():
        count[0] += 1
        return count[0]
    return wrap

def func1():
    m = 2
    n = 3
    def bar():
        return n+m+5
    return bar

def func2(m,n):
    m[0] = 100
    n = 4
    print m,n
    return None

a = [1,2,3]
b = 3
func2(a,b)
print a,b

i = 0
print i
def f():
    #i = 1
    print i
    return None

def func3(data):
    count = data
    def wrap():
        #nonlocal count
        count += 1
        return count
    return wrap
a = func3(3)
a()
