def safe_pawns(pawns):
    count = 0
    for c in pawns:
        if c[0] > 'a' and c[0] < 'h' and c[1] > 1:
            if chr(ord(c[0])-1)+chr(ord(c[1])-1) in pawns or chr(ord(c[0])+1)+chr(ord(c[1])-1) in pawns:
                count += 1
        elif c[0] == 'a' and c[1] > 1:
            if chr(ord(c[0])+1)+chr(ord(c[1])-1) in pawns:
                count += 1
        elif c[0] == 'h' and c[1] > 1:
            if chr(ord(c[0])-1)+chr(ord(c[1])-1) in pawns:
                count += 1           
    return count

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
    assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1

