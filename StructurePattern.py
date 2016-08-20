'''
Created on 2016/1/26/

@author: HKJ
'''
def decimal2number(decimal_number,base):
    table = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    for i in range(10):
        table[i] = str(i)
    dec_n=decimal_number
    result = []
    while dec_n >= base:
        dec_n,mod = divmod(dec_n,base)
        result.append(table[mod])
    result.append(table[dec_n])
    result.reverse()
    return ''.join(result)
def check_structure_2(pattern, structure):
    pattern = bin(pattern)[2::]
    if len(pattern) > len(structure):
        return False
    else:
        #pattern.zfill(len(structure))
        pattern = '0'*(len(structure)-len(pattern))+pattern
        for i in range(len(structure)):
            if ((pattern[i] == '0' and structure[i].isdigit()) or \
                (pattern[i] == '1' and structure[i].isalpha()))==False:
                return False
        return True
def check_structure_3(pattern, structure):
    pattern = decimal2number(pattern,3)
    if len(pattern) > len(structure):
        return False
    else:
        #pattern.zfill(len(structure))
        pattern = '0'*(len(structure)-len(pattern))+pattern
        for i in range(len(structure)):
            if ((pattern[i] == '0' and structure[i].isdigit()) or \
                (pattern[i] == '1' and structure[i].islower()) or \
                (pattern[i] == '2' and structure[i].isupper()))==False:
                return False
        return True
def check_structure_4(pattern, structure):
    pattern = decimal2number(pattern,4)
    if len(pattern) > len(structure):
        return False
    else:
        #pattern.zfill(len(structure))
        pattern = '0'*(len(structure)-len(pattern))+pattern
        for i in range(len(structure)):
            if ((pattern[i] == '0' and structure[i].isdigit()) or \
                (pattern[i] == '1' and structure[i].islower()) or \
                (pattern[i] == '2' and structure[i].isupper()) or \
                (pattern[i] == '3' and structure[i].isspace()))==False:
                return False
        return True

def check_structure(pattern, structure, pattern_level=2):
    if pattern_level == 2:
        return check_structure_2(pattern, structure)
    elif pattern_level == 3:
        return check_structure_3(pattern, structure)
    elif pattern_level == 4:
        return check_structure_4(pattern, structure)
    else:
        exit("wrong pattern_level")
if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    # Rank 1
    assert check_structure(42, "12a0b3e4"), "42 is the answer"
    assert not check_structure(101, "ab23b4zz"), "one hundred plus one"
    assert check_structure(0, "478103487120470129"), "Any number"
    assert check_structure(127, "Checkio"), "Uppercase"
    assert not check_structure(7, "Hello"), "Only full match"
    assert not check_structure(8, "a"), "Too short command"
    assert check_structure(5, "H2O"), "Water"
    assert not check_structure(42, "C2H5OH"), "Yep, this is not the Answer"

    # Rank 2
    assert check_structure(1823, 'CheckiO', 3), "up and down"
    assert not check_structure(1826, 'CheckiO', 3), "wrong up and down"
    assert check_structure(66431, '9z1b2c4d6a7Z', 3), "Various"

    # Rank 3
    assert not check_structure(39294315, 'Kill Them ALL', 4), "Don't kill"
    assert not check_structure(29, 'aXz', 4), "A Z"
    assert check_structure(39294442, 'Feed Them ALL', 4), "Feed them"
    assert check_structure(2385166685525, 'C3PO and 300 spartans', 4), "C3PO"

    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
