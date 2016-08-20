roman = [{'1':'I','2':'II','3':'III','4':'IV','5':'V','6':'VI','7':'VII','8':'VIII','9':'IX','10':'X'},
         {'1':'X','2':'XX','3':'XXX','4':'XL','5':'L','6':'LX','7':'LXX','8':'LXXX','9':'XC','10':'C'},
         {'1':'C','2':'CC','3':'CCC','4':'CD','5':'D','6':'DC','7':'DCC','8':'DCCC','9':'CM','10':'M'},
         {'1':'M','2':'MM','3':'MMM'}]
def checkio(data):
    le = str(data)
    s = ''
    if len(le) == 4:
        s += roman[3][le[0]]
        le = le[1:]
    if len(le) == 3:
        if le[0] > '0':
            s += roman[2][le[0]]
            le = le[1:]
    if len(le) == 2:
        if le[0] > '0':
            s += roman[1][le[0]]
            le = le[1:]
    if len(le) == 1:
        if le[0] > '0':
            s += roman[0][le[0]]
            le = le[1:]
        
    return s

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(6) == 'VI', '6'
    assert checkio(76) == 'LXXVI', '76'
    assert checkio(499) == 'CDXCIX', '499'
    assert checkio(3888) == 'MMMDCCCLXXXVIII', '3888'
