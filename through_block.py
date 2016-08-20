from math import floor
def through_block(A,B):
    C = set()
    if A[0] == B[0]:
        if A[1] > B[1]:
            for i in range(B[1]+1,A[1]):
                C.add((A[0],i))
        else:
            for i in range(A[1]+1,B[1]):
                C.add((A[0],i))
        return C
    if A[1] == B[1]:
        if A[0] > B[0]:
            for i in range(B[0]+1,A[0]):
                C.add((A[1],i))
        else:
            for i in range(A[0]+1,B[0]):
                C.add((A[1],i))
        return C
    
    c = 1.0*(abs(A[1] - B[1]) + 1)/(abs(A[0] - B[0]) + 1)
    xs = (B[0]-A[0])/abs(B[0]-A[0])
    ys = (B[1]-A[1])/abs(B[1]-A[1])
    xd = 1 if xs == -1 else 0
    yd = 1 if ys == 1 else 0
    print c
    for i in range(abs(A[0]-B[0])):
        a = A[0] + xs*(i+xd)
        b = A[1]+c*ys*(i+1)-yd
        print a,b
        if floor(b) != b: 
            C.add((int(floor(a)),int(floor(b)+1)))
            C.add((int(floor(a))+1,int(floor(b)+1)))
        else:
            C.add((int(floor(a)),int(floor(b))))
            C.add((int(floor(a)),int(floor(b)+1)))
            C.add((int(floor(a)+1),int(floor(b))))
            C.add((int(floor(a)+1),int(floor(b)+1)))
    print C

    c = 1.0*(abs(A[0] - B[0]) + 1)/(abs(A[1] - B[1]) + 1)
    xs = (B[0]-A[0])/abs(B[0]-A[0])
    ys = (B[1]-A[1])/abs(B[1]-A[1])
    xd = 1 if xs == 1 else 0
    yd = 1 if ys == -1 else 0
    print c
    for i in range(abs(A[1]-B[1])):
        b = A[1] + ys*(i+yd)
        a = A[0]+c*xs*(i+1)-xd
        print a,b
        if floor(a) != a: 
            C.add((int(floor(a)+1),int(floor(b))))
            C.add((int(floor(a)+1),int(floor(b)+1)))
        else:
            C.add((int(floor(a)),int(floor(b))))
            C.add((int(floor(a)),int(floor(b)+1)))
            C.add((int(floor(a)+1),int(floor(b))))
            C.add((int(floor(a)+1),int(floor(b)+1)))
    print C

    C.add(B)
    C.add(A)
    C.remove(B)
    C.remove(A)
    print C
    return C
