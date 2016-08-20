def rotate(state, pipe_numbers):
    result = []
    len_s = len(state)
    for i in range(len_s):
        flag = True
        for c in pipe_numbers:
            if state[(c+len_s-i)%len_s] != 1:
                flag = False
                break
        '''
        if flag == True and i == 0:
            result.append(i)
            break
        elif flag == True:
            result.append(i)
        '''
        if flag == True:
            result.append(i)
    return result


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert rotate([1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1], [0, 1]) == [1, 8], "Example"
    assert rotate([1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1], [0, 1, 2]) == [], "Mission impossible"
    assert rotate([1, 0, 0, 0, 1, 1, 0, 1], [0, 4, 5]) == [0], "Don't touch it"
    assert rotate([1, 0, 0, 0, 1, 1, 0, 1], [5, 4, 5]) == [0, 5], "Two cannonballs in the same pipe"

