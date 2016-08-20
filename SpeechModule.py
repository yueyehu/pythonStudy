'''
Created on 2015/11/26

@author: HKJ
'''
FIRST_TEN = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
SECOND_TEN = ["ten", "eleven", "twelve", "thirteen", "fourteen",
              "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
OTHER_TENS = ["twenty", "thirty", "forty", "fifty",
              "sixty", "seventy", "eighty", "ninety"]
HUNDRED = "hundred"
THOUSAND = "thousand"


def tell_number(number):
    s = ''
    if number == 0:
        return 'zero'
    elif number < 0:
        s = 'minus '
    number = abs(number)
    s1 = tell_num(number%1000)
    s2 = tell_num(number/1000)
    if len(s2):
        s += s2 + THOUSAND + ' '
    s += s1
    return s.strip()
    
def tell_num(number):
    s = ''
    if number == 0:
        return s
    else:
        if number/100 > 0:
            s += FIRST_TEN[number/100-1]+' '+HUNDRED+' '
        if number%100/10 > 1:
            s += OTHER_TENS[number%100/10-2] + ' '
            if number%10 > 0:
                s += FIRST_TEN[number%10-1] +' '
        elif number%100/10 == 1:
            s += SECOND_TEN[number%10] +' '
        else:
            s += FIRST_TEN[number%10-1]
        return s

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    # Rank 1
    assert tell_number(4) == 'four', "1st example"
    assert tell_number(133) == 'one hundred thirty three', "2nd example"
    assert tell_number(12) == 'twelve', "3rd example"
    assert tell_number(101) == 'one hundred one', "4th example"
    assert tell_number(212) == 'two hundred twelve', "5th example"
    assert tell_number(40) == 'forty', "6th example"
    assert not tell_number(212).endswith(' '), "Dont forget strip whitespaces at the end of string"

    # Rank 2
    assert tell_number(-133) == 'minus one hundred thirty three', "Minus"
    assert tell_number(0) == 'zero', "Zero"

    # Rank 3
    assert tell_number(42000) == 'forty two thousand', "42 many"
    assert (tell_number(-999999) ==
            "minus nine hundred ninety nine thousand nine hundred ninety nine"), "Abyss"

    print("Earn cool rewards by using the 'Check' button!")