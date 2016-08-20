# -*- coding: cp936 -*-
'''检测密码的安全性'''

'''自己的方法'''
import re
def checkio(data):
    if len(data) >= 10:
       if re.findall('[a-z]',data) and re.findall('[A-Z]',data) and re.findall('[0-9]',data):
           return True
    return False
    
           
'''方法一'''
import re
def checkio_1(data):
    return re.match("(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])([a-zA-Z0-9]{10,})",data) 
