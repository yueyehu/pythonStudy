def checkio(lines_list):
    """Return the quantity of squares"""
    lines_set = {tuple(c) for c in lines_list}
    count = 0
    for c in lines_set:
        if c[1] - c[0] == 1:
            if len({(c[0],c[0]+4),(c[1],c[1]+4),(c[0]+4,c[1]+4)}&lines_set) == 3:
                count += 1
                print '1',count
            if len({(c[0],c[0]+4),(c[0]+4,c[0]+8),(c[0]+8,c[1]+8),(c[0]+9,c[1]+9),(c[1]+1,c[1]+5),(c[1]+5,c[1]+9),(c[0]+1,c[1]+1)}&lines_set) == 7:
                count += 1
                print '2',count
            if c == (1,2) and len({(c[0],c[0]+4),(c[0]+4,c[0]+8),(c[0]+8,c[0]+12),\
                                   (c[1]+2,c[1]+6),(c[1]+6,c[1]+10),(c[1]+10,c[1]+14),\
                                   (c[0]+12,c[1]+12),(c[0]+13,c[1]+13),(c[0]+14,c[1]+14),\
                                   (c[0]+1,c[1]+1),(c[0]+2,c[1]+2)}&lines_set) == 11:
                count += 1
                print '3',count
    return count


if __name__ == '__main__':
    assert (checkio([[1, 2], [3, 4], [1, 5], [2, 6], [4, 8], [5, 6], [6, 7],
                     [7, 8], [6, 10], [7, 11], [8, 12], [10, 11],
                     [10, 14], [12, 16], [14, 15], [15, 16]]) == 3), "First, from description"
    assert (checkio([[1, 2], [2, 3], [3, 4], [1, 5], [4, 8],
                     [6, 7], [5, 9], [6, 10], [7, 11], [8, 12],
                     [9, 13], [10, 11], [12, 16], [13, 14], [14, 15], [15, 16]]) == 2), "Second, from description"
    assert (checkio([[1, 2], [1, 5], [2, 6], [5, 6]]) == 1), "Third, one small square"
    assert (checkio([[1, 2], [1, 5], [2, 6], [5, 9], [6, 10], [9, 10]]) == 0), "Fourth, it's not square"
    assert (checkio([[16, 15], [16, 12], [15, 11], [11, 10],
                     [10, 14], [14, 13], [13, 9]]) == 0), "Fifth, snake"
