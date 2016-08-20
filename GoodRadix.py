'''
Created on 2016/1/26/

@author: HKJ
'''
def create_radixMap():
    radixMap = {}
    for i in range(0,10):
        radixMap[str(i)] = i+1
    for i in range(0,26):
        radixMap[chr(ord('A')+i)] = 11+i
    return radixMap
def count_result(str_number,base,radixMap):
    l = len(str_number)
    s = 0
    for i,c in enumerate(str_number):
        s += (radixMap[c]-1)*base**(l-i-1)
    return s
def good_radix(str_number):
    radixMap = create_radixMap()
    for k in range(radixMap[max(list(str_number))],37):
        if count_result(str_number,k,radixMap)%(k-1) == 0:
            return k
    return 0


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert good_radix("18") == 10, "Simple decimal"
    assert good_radix("1010101011") == 2, "Any number is divisible by 1"
    assert good_radix("222") == 3, "3rd test"
    assert good_radix("A23B") == 14, "It's not a hex"
    assert good_radix("IDDQD") == 0, "k is not exist"


    print("Now that you're finished, hit the 'Check' button to review your code and earn sweet rewards!")
