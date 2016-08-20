def convert(str_number, radix):
    d = dict()
    for i in range(10):
        d[chr(ord('0')+i)] = i
    for i in range(10,36):
        d[chr(ord('A')+i-10)] = i
    sum = 0
    for i,c in enumerate(str_number):
        if d[c] > radix:
            return -1
        else:
            sum += d[c]*(radix**(len(str_number)-1-i))
    return sum


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert convert("AF", 16) == 175, "Hex"
    assert convert("101", 2) == 5, "Bin"
    assert convert("101", 5) == 26, "5 base"
    assert convert("Z", 36) == 35, "Z base"
    assert convert("AB", 10) == -1, "B > A > 10"

    print("Use 'Check' to earn sweet rewards!")
