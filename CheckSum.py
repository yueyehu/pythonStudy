'''
Created on 2015/12/16/

@author: HKJ
'''
import re
def checkio(data):
    data = re.findall('[A-Z0-9a-z]',data)[::-1]
    s = 0
    for i,d in enumerate(data):
        if i%2 == 0:
            s += sum(map(int,str((ord(d)-48)*2)))
        else:
            s += ord(d)-48 
    #replace this for solution
    result = 10-s%10
    if s % 10 == 0:
        return ['0',s]
    else:
        return [str(result), s]

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert (checkio(u"799 273 9871") == ["3", 67]), "First Test"
    assert (checkio(u"139-MT") == ["8", 52]), "Second Test"
    assert (checkio(u"123") == ["0", 10]), "Test for zero"
    assert (checkio(u"999_999") == ["6", 54]), "Third Test"
    assert (checkio(u"+61 820 9231 55") == ["3", 37]), "Fourth Test"
    assert (checkio(u"VQ/WEWF/NY/8U") == ["9", 201]), "Fifth Test"

    print("OK, done!")