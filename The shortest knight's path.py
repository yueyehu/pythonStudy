def possible_pos(f):
    result = []
    if chr(ord(f[0])+1)<='h' and chr(ord(f[1])+2)<='8':
        result.append(chr(ord(f[0])+1)+chr(ord(f[1])+2))
    if chr(ord(f[0])+1)<='h' and chr(ord(f[1])-2)>='1':
        result.append(chr(ord(f[0])+1)+chr(ord(f[1])-2))
    if chr(ord(f[0])-1)>='a' and chr(ord(f[1])+2)<='8':
        result.append(chr(ord(f[0])-1)+chr(ord(f[1])+2))
    if chr(ord(f[0])-1)>='a' and chr(ord(f[1])-2)>='1':
        result.append(chr(ord(f[0])-1)+chr(ord(f[1])-2))

    if chr(ord(f[1])+1)<='8' and chr(ord(f[0])+2)<='h':
        result.append(chr(ord(f[0])+2)+chr(ord(f[1])+1))
    if chr(ord(f[1])+1)<='8' and chr(ord(f[0])-2)>='a':
        result.append(chr(ord(f[0])-2)+chr(ord(f[1])+1))
    if chr(ord(f[1])-1)>='1' and chr(ord(f[0])+2)<='h':
        result.append(chr(ord(f[0])+2)+chr(ord(f[1])-1))
    if chr(ord(f[1])-1)>='1' and chr(ord(f[0])-2)>='a':
        result.append(chr(ord(f[0])-2)+chr(ord(f[1])-1))
    return result
        
def isfind(f,t):
    if t in possible_pos(f):
        return True
    else:
        return False

def find_min(f,t,visit_set):
    if isfind(f,t) == True:return 1
    pos = possible_pos(f)
    count_min = 1000000
    for p in pos:
        if p in visit_set:continue
        visit = visit_set.copy()
        visit.add(p)
        if len(visit) > 10:break
        #print visit
        count = find_min(p,t,visit) + 1
        if count_min > count:count_min = count
        if count_min == 2: break
    return count_min

def checkio(cells):
    f_t = cells.split('-')
    visit_set = set()
    visit_set.add(f_t[0])
    return find_min(f_t[0],f_t[1],visit_set)
'''
if __name__ == "__main__":
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(u"b1-d5") == 2, "1st example"
    assert checkio(u"a6-b8") == 1, "2nd example"
    assert checkio(u"h1-g2") == 4, "3rd example"
    assert checkio(u"h8-d7") == 3, "4th example"
    assert checkio(u"a1-h8") == 6, "5th example"
'''
