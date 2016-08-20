from math import ceil as c
def golf(r):  
 t=p=0
 y=r
 for x in range(1,int(c(r))):
  h=(r**2-x**2)**0.5
  t+=int(h)
  p+=int(c(y))-int(h)
  y=h
 p+=int(c(y))
 return [t*4,p*4]
