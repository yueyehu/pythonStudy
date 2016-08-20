def checkio(number):
    if number == 1:return ''
    min_d = 0
    for i in range(2,10):
        s = ''
        if number/i == number*1.0/i:
            s = chr(i+ord('0'))+str(checkio(number/i))
            s = list(s)
            s.sort()
            s = int(''.join(s))
            if min_d == 0:min_d = s
            if min_d > s:min_d = s
    num = [ord(x)-ord('0') for x in str(min_d)]
    if number == reduce(lambda x,y:x*y,num):return min_d
    else:return 0

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(20) == 45, "1st example"
    assert checkio(21) == 37, "2nd example"
    assert checkio(17) == 0, "3rd example"
    assert checkio(33) == 0, "4th example"
    assert checkio(3125) == 55555, "5th example"
    assert checkio(9973) == 0, "6th example"
