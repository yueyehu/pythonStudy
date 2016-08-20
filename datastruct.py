# -*- coding: cp936 -*-
import re
import string
def word_flu_count():
    '''13.1'''
    fin = open('article1.txt')
    spc = string.punctuation
    d = dict()
    for line in fin:
        li = list(line)
        for c in range(len(li)):
            if li[c] in spc:
                li[c] = ""
        line = ''.join(li)
        line = line.strip()
        word = re.split(' ',line)
        for w in word:
            w = w.lower()
            if w in d:
                d[w] = d[w]+1
            else:
                d[w]=1
    return d

def word_flu_count_1():
    '''13.1 正则表达式'''
    fin = open('article1.txt')
    d = dict()
    for line in fin:
        line = re.findall(r'[a-zA-Z]+',line)
        for w in line:
            w = w.lower()
            if w in d:
                d[w] += 1
            else:
                d[w] = 1
    return d
                
def word_max_flu(d):
    '''13-3'''
    li = list()
    max_d = dict()
    N = 20
    for i in d:
        li.append(d[i])
    li.sort(reverse = True)
    li = li[0:N]
    count = 0
    while count <= N:
        for w in d:
            if d[w] in li:
                max_d[w] = d[w]
                count += 1
    return max_d
def dict_c():
    '''13-4'''
    li = list()
    fin = open('words.txt')
    for line in fin:
        line = line.strip()
        li.append(line)
    return li

def count_worng():
    '''13-4'''
    lis = list()
    d = word_flu_count_1()
    li = dict_c()
    for w in d:
        if w not in li:
            lis.append(w)
    return lis

print count_worng()

