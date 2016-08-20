import string
file1 = open('2.txt','r')
#ss = {'m':'k','q':'o','g':'e'}
#ss = {'k':'m','o':'q','e':'g'}
li = []

for line in file1:
    for c in line:
        '''
        if c in ss.keys():
            li.append(ss[c])
        else:
            li.append(c)
        '''
        if ord(c) >= ord('a') and ord(c) <= ord('x'):
            li.append(chr(ord(c)+2))
        elif ord(c) >= ord('y') and ord(c) <= ord('z'):
            li.append(chr((ord(c)+2)%ord('z')+ord('a')-1))
        else:
            li.append(c)
file1.close()
print ''.join(li)

