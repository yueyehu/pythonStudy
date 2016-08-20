from math import acos
from math import pi
def angles(a, b, c):
    if a+b>c and a+c>b and b+c>a:
        theta1 = round(acos(((a**2+b**2-c**2)/(2.0*a*b)))/(2*pi)*360)
        theta2 = round(acos(((a**2+c**2-b**2)/(2.0*c*a)))/(2*pi)*360)
        theta3 = round(acos(((c**2+b**2-a**2)/(2.0*c*b)))/(2*pi)*360)
        ang = [theta1,theta2,theta3]
        ang.sort()
        return ang
    return [0, 0, 0]


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert angles(4, 4, 4) == [60, 60, 60], "All sides are equal"
    assert angles(3, 4, 5) == [37, 53, 90], "Egyptian triangle"
    assert angles(2, 2, 5) == [0, 0, 0], "It's can not be a triangle"

    print("Code's finished? Earn rewards by clicking 'Check' to review your tests!")
