import re
def strback(s):
    for i in range(len(s)):
        print s[-1-i]

#prefixes = ['J','K','M','N','Ou','P','Qu']
'''8-1'''
prefixes = 'JKMNOPQ'
suffix = 'ack'
for c in prefixes:
    if c == 'O' or c == 'Q':
        c = c + 'u'
    print c+'ack'

def findindex(word,letter,index):
    '''8-4'''
    for i in range(len(word)):
        if i+index < len(word):
#            print i+index,len(word)
            if word[i+index] == letter:
                return i + index
        else:
            break

def strcount(word,letter):
    '''8-5'''
    num = 0
    for i in range(len(word)):
        if i+len(letter) <= len(word):
            if word[i:i+len(letter)] == letter:
                num += 1
        else:
            break
    return num
        
        
def in_both(s1,s2):
    '''8.9'''
    store = []
    for c1 in s1:
        if c1 not in store:
            if c1 in s2:
                store += c1
    return store

def is_reverse(s1,s2):
    '''8.11'''
    if len(s1) != len(s2):
        return False
    for i in range(len(s1)):
        if s1[i] != s2[-1-i]:
            return False
    return True

def is_palindrome(s1):
    '''8-10'''
    if s1 == s1[::-1]:
        return True
    return False

def rotate_word(s1,n):
    '''8-12'''
    s2 = str()
    for c in s1:
        if c.islower():
            if ord(c)+n < ord('a'):
                s2 += chr(ord(c)+n+26)
            elif ord(c)+n > ord('z'):
                s2 += chr(ord(c)+n-26)
            else:
                s2 += chr(ord(c)+n)
        else:
            if ord(c)+n < ord('A'):
                s2 += chr(ord(c)+n+26)
            elif ord(c)+n > ord('Z'):
                s2 += chr(ord(c)+n-26)
            else:
                s2 += chr(ord(c)+n)      
    return s2
   
def getword(s1):
    '''9-1'''
    fin = open(s1)
    for line in fin:
        word = line.strip()
        if len(word) > 20:
            print word

def count_letter_rate(s1,letter):
    '''9-2'''
    totalnum = 0
    num = 0
    fin = open(s1)
    for line in fin:
        word = line.strip()
        word = word.lower()
        letter = letter.lower()
        if letter in word:
            num += 1
        totalnum += 1
    return 1.0*num/totalnum

def count_rate(s1):
    '''9-2 extend'''
    l_d = dict()
    f = ord('a')
    for i in range(26):
        l_d[chr(f+i)] = count_letter_rate(s1,chr(f+i))
    return l_d

def avoids(s1,s2):
    '''9-3'''
    for c in s2:
        if c in s1:
            return False
    return True

def find_not_avoids(s1,s2):
    '''9-3'''
    count = 0
    t = re.split(',|\s|;|\.|\(|\)|\'|\"',s1)
    print t
    for word in t:
        if avoids(word,s2):
            print word
            count +=1
    return count

def is_abecedarian(word):
    '''9-6'''
    word.islower()
    temp = word[0]
    for c in word:
        if temp > c:
            return False
        temp = c
#    print word
    return True

def count_abecedarian(file):
    '''9-6'''
    fin = open(file)
    count = 0
    for line in fin:
        word = line.strip()
        if is_abecedarian(word):
            count += 1
    return count

def cartalk1(word):
    '''9-7'''
    for i in range(len(word)):
        j=0
        while word.count(word[i+j]) >= 3:
            if word[i+j] != word[i+j+1]:
                j += 1
    

        
















