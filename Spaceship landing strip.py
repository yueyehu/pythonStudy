def checkio(landing_map):
    landing_map = [[1 if i=='G' or i=='S' else 0 for i in s]for s in landing_map]
    print landing_map
    count_r = 0
    max_field = 0
    while count_r < len(landing_map):
        count_c = 0
        while count_c < len(landing_map[0]):
            if landing_map[count_r][count_c] == 1:
                i = count_r
                j = list()
                max_temp = 0
                while i < len(landing_map):
                    
                    if landing_map[i][count_c] == 1:
                        j.append(count_c)
                    else:
                        break
                    
                    while j[-1] < len(landing_map[0]):
                        if landing_map[i][j[-1]] == 1:
                            j[-1] += 1
                        else:
                            break
                    #print 'count_r',count_r,'i',i,'count_c',count_c,'j',j
                    max_temp = (i-count_r+1)*(min(j)-count_c) if (i-count_r+1)*(min(j)-count_c) > max_temp else max_temp
                    i += 1
                    
                max_field = max_temp if max_temp > max_field else max_field
            count_c += 1
        count_r += 1
                
    return max_field

'''
if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([u'G']) == 1, 'One cell - one variant'
    assert checkio([u'GS',
                    u'GS']) == 4, 'Four good cells'
    assert checkio([u'GT',
                    u'GG']) == 2, 'Four cells, but with a tree'
    assert checkio([u'GGTGG',
                    u'TGGGG',
                    u'GSSGT',
                    u'GGGGT',
                    u'GWGGG',
                    u'RGTRT',
                    u'RTGWT',
                    u'WTWGR']) == 9, 'Classic'
'''
