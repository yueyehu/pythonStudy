# -*- coding: cp936 -*-
def count_c(filename):
    '''统计字母频率'''
    fin = open(filename)
    w_d = dict()
    count = 0
    try:
        for line in fin:
            line = line.strip()
            line = line.lower()
            for c in line:
                count += 1
                if c in w_d:
                    w_d[c] += 1
                else:
                    w_d[c] = 1
    finally:
        fin.close()
    for w in w_d:
        w_d[w] /=(1.0*count)
    return w_d

def sort_dict(d):
    '''给字典从大到小排序'''
    l_d = list()
    for w in d:
       l_d.append([w,d[w]])
    for i in range(len(l_d)-1):
        for j in range(len(l_d)-i-1):
            if l_d[j][1] < l_d[j+1][1]:
                temp = l_d[j]
                l_d[j] = l_d[j+1]
                l_d[j+1] = temp
    return l_d

def write_data(filename,l_d):
    '''将列表中的数据写入文档'''
    fin = open(filename,'w')
    try:
        for i in range(len(l_d)):
            fin.write(l_d[i][0]+':'+str(l_d[i][1])+'\n')
    finally:
        fin.close()
        
d = count_c('words.txt')
l_d = sort_dict(d)
write_data('w.txt',l_d)
