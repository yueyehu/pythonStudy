# -*- coding: cp936 -*-
'''Ѱ����λ��'''
def checkio(data):
    '''�Լ��ķ���'''
    data.sort()
    if len(data)%2 == 1:
        return data[len(data)/2]
    else:
        return (data[len(data)/2]+data[len(data)/2-1])/2.0
