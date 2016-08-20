def checkio(opacity):
    Fibonacci  = map(lambda x,f=lambda x,f:(f(x-1,f)+f(x-2,f)) if x>1 else 1: f(x,f),range(1,21))
    opacity_c = 10000
    for year in xrange(0,10001):
        if year in Fibonacci or year == 0:
            opacity_c -= year
        else:
            opacity_c += 1
        if opacity == opacity_c:
            return year
    return year

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(10000) == 0, "Newborn"
    assert checkio(9999) == 1, "1 year"
    assert checkio(9997) == 2, "2 years"
    assert checkio(9994) == 3, "3 years"
    assert checkio(9995) == 4, "4 years"
    assert checkio(9990) == 5, "5 years"
