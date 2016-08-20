'''
Created on 2015/11/24

@author: HKJ
'''
import re
golf=lambda r:sum(9*(ord(d[0])-ord('A'))+int(d[1])for d in re.findall('[A-Z][1-9]',r))
