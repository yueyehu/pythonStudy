A = [1,2,3]
def func():
    B = A
    def func1():
        B[0] = [2,3,4]
        print B
    func1()
    print B
    return None
func()

def func1(data):
    saved = [data]
    def f():
        saved[0] += 1
        return saved[0]
    return f
L = [1,2,3]
print id(L),L
def func2():
    global L
    L = [2,3,4]
    print L
func2()
print id(L),L
