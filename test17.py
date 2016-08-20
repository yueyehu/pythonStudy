# -*- coding: cp936 -*-
'''数字发声'''

'''自己的方法'''
FIRST_TEN = ["one", "two", "three", "four", "five", "six", "seven",
             "eight", "nine"]
SECOND_TEN = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
              "sixteen", "seventeen", "eighteen", "nineteen"]
OTHER_TENS = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy",
              "eighty", "ninety"]
HUNDRED = "hundred"


def checkio(number):
    n = str(number)
    s = ''
    if len(n) == 3:
        s = FIRST_TEN[int(n[0])-1] +' '+ HUNDRED
        n = n[1:]
    if len(n) == 2 and int(n[0]) > 1:
        s = s + ' ' + OTHER_TENS[int(n[0])-2]
        n = n[1:]
    elif len(n) == 2 and int(n[0]) == 1:
        return (s + ' ' +SECOND_TEN[int(n[1])]).lstrip()
    elif len(n) == 2 and int(n[0]) == 0:
        n = n[1:]
    if int(n[0]) > 0: 
        return (s + ' ' + FIRST_TEN[int(n[0])-1]).lstrip()
    else:
        return s.lstrip()
