def checkio(data):
    x1,y1 = ord(data[1])-ord(u'0'),ord(data[3])-ord(u'0')
    x2,y2 = ord(data[7])-ord(u'0'),ord(data[9])-ord(u'0')
    x3,y3 = ord(data[-4])-ord(u'0'),ord(data[-2])-ord(u'0')
    x0 = ((x2**2+y2**2-x1**2-y1**2)*(y3-y2)-(x3**2+y3**2-x2**2-y2**2)*(y2-y1))*1.0/((y2-y1)*(x2-x3)-(y3-y2)*(x1-x2))/2
    y0 = ((x1**2+y1**2-x2**2-y2**2)*(x2-x3)-(x2**2+y2**2-x3**2-y3**2)*(x1-x2))*1.0/((y3-y2)*(x1-x2)-(y2-y1)*(x2-x3))/2
    r = ((x1-x0)**2+(y1-y0)**2)**0.5
    x0 = int(round(x0,2)) if round(x0,2) == int(round(x0,2)) else round(x0,2)
    y0 = int(round(y0,2)) if round(y0,2) == int(round(y0,2)) else round(y0,2)
    r  = int(round(r,2)) if round(r,2) == int(round(r,2)) else round(r,2)
    return '(x-%r)^2+(y-%r)^2=%r^2'%(x0,y0,r)

#These "asserts" using only for self-checking and not necessary for auto-testing

if __name__ == '__main__':
    assert checkio(u"(2,2),(6,2),(2,6)") == "(x-4)^2+(y-4)^2=2.83^2"
    assert checkio(u"(3,7),(6,9),(9,7)") == "(x-6)^2+(y-5.75)^2=3.25^2"

