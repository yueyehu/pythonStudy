# -*- coding: cp936 -*-
'''选择重复的数，不得改变顺序'''
def checkio(data):
    '''自己的方法'''
    for i,d in enumerate(data):
        data[i] = None
        if d in data:
            data[i] = d
    return [x for x in data if x != None]


'''方法一'''
import collections

def checkio_1(data):
    counter = collections.Counter(data)
    return [item for item in data if counter[item] > 1]

'''方法二'''
from collections import Counter

def checkio_2(data):
    return [e for e in data if Counter(data)[e] > 1]

'''方法三'''
def checkio_3(data):
    return filter(lambda x:data.count(x) !=1,data)
