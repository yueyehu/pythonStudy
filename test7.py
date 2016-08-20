import sys
sys.path.append('C:\\ThinkBayes')
from thinkbayes import Pmf

pmf = Pmf()
for x in range(6):
    pmf.Set(x,1/6.0)
