# -*- coding: cp936 -*-
import re
def fine_word():
    '''��һ�λ��еĵ�����������'''
    fin = open('article.txt')
    for line in fin:
        lin = re.findall(r'[a-zA-Z]+',line)
        print lin

fine_word()
