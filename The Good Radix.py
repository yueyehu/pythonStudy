def checkio(number):
    number = number.lower()
    num_map = {}
    count = 0
    for i in range(10):
        num_map[str(i)] = count
        count += 1
    for i in range(26):
        num_map[chr(ord('a')+i)] = count
        count += 1
    max_number = 0
    for c in number:
        if num_map[c] > max_number:
            max_number = num_map[c]
    #print max_number
    for radix in range(max_number+1,37):
        dec_number = 0
        for i,c in enumerate(number):
            dec_number += num_map[c]*radix**(len(number)-i-1)
        #print dec_number
        if dec_number%(radix-1) == 0:return radix
    return 0

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(u"18") == 10, "Simple decimal"
    assert checkio(u"1010101011") == 2, "Any number is divisible by 1"
    assert checkio(u"222") == 3, "3rd test"
    assert checkio(u"A23B") == 14, "It's not a hex"
    assert checkio(u"IDDQD") == 0, "k is not exist"
    print('Local tests done')

