'''
Created on 2015Äê11ÔÂ25ÈÕ

@author: HKJ
'''
from math import pi,atanh,asin
#golf=lambda h,w:(round(pi*w*w*h/6,2),round(pi*(w**2+h**2*(acos(w/h)/tan(acos(w/h))if w<h elif w>h atanh(sin(acos(h/w)))/sin(acos(h/w))))/2,2))
#def golf(h,w):
#    e=acos(w/h if w<h else h/w)
#    if w<h:d=e/tan(e)
#    elif w>h:d=atanh(sin(e))/sin(e)
#    else:d=1
#    return round(pi*w*w*h/6,2),round(pi*(w**2+h**2*d)/2,2)
'''
def golf(h,w):
 if w<h:
  e=acos(w/h)
  d=e/tan(e)
 elif w>h:
  e=sin(acos(h/w))
  d=atanh(e)/e
 else:d=1
 return round(pi*w*w*h/6,2),round(pi*(w**2+h**2*d)/2,2)
# return map(lambda k:round(k*pi/2,2),[w*w*h/3,w**2+h**2*d])
'''
'''
def golf(h,w):
    h,w,p=h/2,w/2,1.6075
    return round(4*pi*w*w*h/3,2),round(4*pi*((w**(2*p)+2*(w*h)**p)/3)**(1/p),2)
'''
        
