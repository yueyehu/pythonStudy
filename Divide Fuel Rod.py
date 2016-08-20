def joint(start,number,div):
    if start*(start+1)/2 > number:
        return -1
    elif start*(start+1)/2 == number:
        div.append(number)
        return 0
    else:
        div.append(start*(start+1)/2)
        return joint(start+1,number-start*(start+1)/2,div)
def disjoint(number):
    for i in range(1,int((2*number)**0.5)):
        div = []
        if joint(i,number,div) == 0:
            return div
    return []

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert disjoint(64) == [15, 21, 28], "1st example"
    assert disjoint(371) == [36, 45, 55, 66, 78, 91], "1st example"
    assert disjoint(225) == [105, 120], "1st example"
    assert disjoint(882) == [], "1st example"

    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
