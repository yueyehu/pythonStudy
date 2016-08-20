def histogram(s):
    cs = dict()
    for c in s:
        if c not in cs:
            cs[c] = 1
        else:
            cs[c] += 1
    return cs

def histogram_c(s):
    '''11-2'''
    cs = dict()
    for c in s:
        cs[c] = cs.get(c,0)+1
    return cs

def print_dict(h):
    for c in h:
        print c,h[c]

def return_keys(h):
    '''11-3'''
    k = h.keys()
    for c in k:
        print c,h[c]
    return k
        
def reverse_lookup(v,h):
    '''11-4'''
    li = list()
    for k in h:
        if h[k] == v:
            li.append(k)
    return li

def invert_dict(d):
    nd = dict()
    for k in d:
        if d[k] not in nd:
            nd[d[k]] = [k]
        else:
            nd[d[k]].append(k)
    return nd
