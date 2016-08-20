def through_count(p1,p2,p3,p4):
    '''(p1,p2) througn (p3,p4)'''
    f = lambda p:(p1[1] - p2[1])*1.0/(p1[0]-p2[0])*(p[0]-p1[0])+p1[1]-p[1]
    print p1,p2,p3,p4
    print f(p3),f(p4)
    if f(p3)*f(p4) < 0:
        a = p2[1] - p1[1]
        b = p2[0] - p1[0]
        e = -(p2[0]-p1[0])*p1[1]+(p2[1]-p1[1])*p1[0]

        c = p4[1] - p3[1]
        d = p4[0] - p3[0]
        f = -(p4[0]-p3[0])*p3[1]+(p4[1]-p3[1])*p3[0]
        x = (d*e-b*f)*1.0/(a*d-b*c)
        print a,b,c,d,e,f,x
        if (p1[0] > p2[0] and p1[0] > x) or (p1[0] < p2[0] and p1[0] < x):
            return 1
        return 0
    elif f(p3) == 0 and f(p4)>0:
        if (p1[0] > p2[0] and p1[0] > p3[0]) or (p1[0] < p2[0] and p1[0] < p3[0]):
            return 1
        return 0
    elif f(p4) == 0 and f(p3)>0:
        if (p1[0] > p2[0] and p1[0] > p4[0]) or (p1[0] < p2[0] and p1[0] < p4[0]):
            return 1
        return 0
    else:
        return 0
def is_inside(polygon, point):
    if point in polygon:return True
    p_len = len(polygon)
    t_count = 0
    #global t_point
    for p in polygon:
        if p[0]!= point[0] and p[1]!= point[1]:
            t_point = p
            break
    try:
        print t_point
    except:
        for p in polygon:
            if p[0]!= point[0]:
                t_point = p
                break
    for i in range(-1,p_len-1):
        #k1 = (point[0] - polygon[(i+p_len)%p_len][0])*1.0/(point[1] - polygon[(i+p_len)%p_len][1])
        #k2 = (point[0] - polygon[(i+p_len+1)%p_len][0])*1.0/(point[1] - polygon[(i+p_len+1)%p_len][1])
        #if k1 == k2: return True
        #if point[0] == polygon[(i+p_len+1)%p_len][0])
        print t_count
        t_count += through_count(point,t_point,polygon[(i+p_len)%p_len],polygon[(i+p_len+1)%p_len])
    print t_count
    return True if t_count%2 == 1 else False


if __name__ == '__main__':
    assert is_inside(((1, 1), (1, 3), (3, 3), (3, 1)),
                     (2, 2)) == True, "First"
    assert is_inside(((1, 1), (1, 3), (3, 3), (3, 1)),
                     (4, 2)) == False, "Second"
    assert is_inside(((1, 1), (4, 1), (2, 3)),
                     (3, 2)) == True, "Third"
    assert is_inside(((1, 1), (4, 1), (1, 3)),
                     (3, 3)) == False, "Fourth"
    assert is_inside(((2, 1), (4, 1), (5, 3), (3, 4), (1, 3)),
                     (4, 3)) == True, "Fifth"
    assert is_inside(((2, 1), (4, 1), (3, 2), (3, 4), (1, 3)),
                     (4, 3)) == False, "Sixth"
    assert is_inside(((1, 1), (3, 2), (5, 1), (4, 3), (5, 5), (3, 4), (1, 5), (2, 3)),
                     (3, 3)) == True, "Seventh"
    assert is_inside(((1, 1), (1, 5), (5, 5), (5, 4), (2, 4), (2, 2), (5, 2), (5, 1)),
                     (4, 3)) == False, "Eighth"
