# -*- coding: cp936 -*-
'''�ҳ�Ƶ����ߵ���ĸ'''

'''�Լ��ķ���'''
def checkio(text):
    d = {}
    text = text.lower()
    for c in text:
        if c >= 'a' and c <= 'z':
            if c in d:
                d[c] += 1
            else:
                d[c] = 1
                temp = c
    for k in d:
        if d[k] > d[temp] or (d[k] == d[temp] and temp > k):
            temp = k
            
    return temp

'''��һ�ַ���'''
import collections

def checkio_1(text):

    freq_list = collections.Counter(filter(str.isalpha, text.lower())).most_common()

    most_freq_count = max(freq[1] for freq in freq_list)

    return sorted([freq[0] for freq in freq_list if freq[1] == most_freq_count])[0]

