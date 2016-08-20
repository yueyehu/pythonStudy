# -*- coding: cp936 -*-
'''寻找中位数'''
def checkio(data):
    '''自己的方法'''
    data.sort()
    if len(data)%2 == 1:
        return data[len(data)/2]
    else:
        return (data[len(data)/2]+data[len(data)/2-1])/2.0
