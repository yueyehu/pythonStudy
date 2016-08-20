import re
def checkio(expression):
    exp = ''.join(re.findall('[{}()[\]]*',expression))
    exp_stack = list()
    for c in exp:
        try:
            if c == u'(' or c == u'{' or c == u'[':exp_stack.append(c)
            elif c == u')' and exp_stack.pop(-1) != u'(':return False
            elif c == u']' and exp_stack.pop(-1) != u'[':return False
            elif c == u'}' and exp_stack.pop(-1) != u'{':return False
        except:
            return False
    if len(exp_stack) == 0:return True
    else:return False

#These "asserts" using only for self-checking and not necessary for auto-testing

if __name__ == '__main__':
    assert checkio(u"((5+3)*2+1)") == True, "Simple"
    assert checkio(u"{[(3+1)+2]+}") == True, "Different types"
    assert checkio(u"(3+{1-1)}") == False, ") is alone inside {}"
    assert checkio(u"[1+1]+(2*2)-{3/3}") == True, "Different operators"
    assert checkio(u"(({[(((1)-2)+3)-3]/3}-3)") == False, "One is redundant"
    assert checkio(u"2+3") == True, "No brackets, no problem"

