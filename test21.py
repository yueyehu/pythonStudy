def checkio(number):
    res_n = number
    count = 0
    for i in xrange(1,number+1):
        if res_n > count + i:
            count += i
            res_n -= count
        elif res_n > count:             
            count = res_n
            break
        else:
            break
    return count

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(1) == 1, "1st example"
    assert checkio(2) == 1, "2nd example"
    assert checkio(5) == 3, "3rd example"
    assert checkio(10) == 6, "4th example"
