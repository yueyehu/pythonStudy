# -*- coding: cp936 -*-
import re
def fine_word():
    '''将一段话中的单词提炼出来'''
    fin = open('article.txt')
    for line in fin:
        lin = re.findall(r'[a-zA-Z]+',line)
        print lin

fine_word()
