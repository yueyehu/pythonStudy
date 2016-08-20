from matplotlib.pyplot import *
import numpy as np
x = np.linspace(-4,4,200)
f1 = np.power(10,x)
f2 = np.power(2.7,x)
f3 = np.power(2,x)

plot(x,f1,'r',x,f2,'b',x,f3,'g',linewidth = 2)
axis([-4,4,-0.5,8])
text(1,7.5,r'$10^x$',fontsize=16)
text(2.2,7.5,r'$e^x$',fontsize=16)
text(3.2,7.5,r'$2^x$',fontsize=16)
title('A simple example',fontsize=16)

savefig('power.png',dpi=75)
show()
