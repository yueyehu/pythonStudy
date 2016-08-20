'''
Created on 2015Äê12ÔÂ1ÈÕ

@author: HKJ
'''
from fractions import Fraction
def divide_pie(groups):
    amount = sum(abs(i) for i in groups)
    if amount == sum(groups):
        return 0,1
    remain = Fraction(1)
    for d in groups:
        if d > 0:
            remain -= Fraction(d,amount)
        elif d < 0:
            remain *= Fraction(amount+d,amount)
    return remain.numerator,remain.denominator
             

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert isinstance((2, -2), (tuple, list)), "Return tuple or list"
    assert tuple(divide_pie((2, -1, 3))) == (1, 18), "Example"
    assert tuple(divide_pie((1, 2, 3))) == (0, 1), "All know about the pie"
    assert tuple(divide_pie((-1, -1, -1))) == (8, 27), "One by one"
    assert tuple(divide_pie((10,))) == (0, 1), "All together"
    print("Code's finished? Earn rewards by clicking 'Check' to review your tests!")