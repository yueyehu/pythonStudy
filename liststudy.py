def nested_sum(t):
    '''10-1'''
    s = 0
    for it in t:
        for i in it:
            s += i
    return s

def list_sum(t):
    '''10-1 extend'''
    s = 0
    for it in t:
        if type(it) == list:
            s += list_sum(it)
        else:
            s += it
    return s

def capitalize_all(s):
    '''10-2'''
    return s.upper()

def capitalize_list(t):
    '''10-2'''
    return map(capitalize_all,t)
    
def list_add(t):
    '''10-3'''
    i = 0
    while i < len(t)-1:
        t[i+1] = t[i+1] + t[i]
        i += 1
    return t

def middle(t):
    '''10-4'''
    del t[0]
    del t[len(t)-1]
    return t

def is_sorted(t):
    '''10-6'''
    for i in range(len(t)-1):
        if t[i] <= t[i+1]:
            continue
        else:
            return False
    return True
        
def is_anagram(t1,t2):
    '''10-7'''
    if len(t1) != len(t2):
        return False
    for c1 in t1:
        if c1 not in t2:
            return False
    return True

def has_duplicates(t):
    '''10-8-1'''
    for c in t:
        t1 = t+[]    
        t1.remove(c)
        if c in t1:
            #print c
            #print t1
            return True 
    return False
        
from random import randint 
def birthday():
    '''10-8-2'''
    t = list()
    for i in range(23):
        t.append([randint(1,12),randint(1,31)])
    return t

def birthday_dup_rate():
    '''10-8-2'''
    count = 0
    for i in range(100):
        t = birthday()
        if has_duplicates(t):
            count = count + 1
    return count/100.0





















