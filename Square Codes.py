def count_squares(*lines_list):
    """Return the quantity of squares"""
    lines_set = {tuple(c) if c[0]<c[1] else tuple([c[1],c[0]])for c in lines_list}
    line = 4
    destroy_point = set() 
    for c in lines_set:
        if c[0] > 16 or c[1]>16:
            line = 5
        if c[0] == 0:
            destroy_point.add(c[1])
    destroy_set = set()
    for p in destroy_point:
        for c in lines_set:
            if p in c:
                destroy_set.add(c)
    lines_set -= destroy_set
    print destroy_point
    print destroy_set
    print lines_set
    count = 0
    for c in lines_set:
        if c[1] - c[0] == 1:
            for i in range(1,line+1):
                for j in range(1,i+1):
                    print i,j
                    print (c[0]+j-1,c[0]+j),(c[0]+line*(j-1)+i,c[0]+i+line*(j)),(c[0]+line*(j-1),c[0]+line*(j)),(c[0]+line*i,c[1]+line*i)
                    if (c[0]+j-1,c[0]+j) not in lines_set or\
                    (c[0]+line*(j-1)+i,c[0]+i+line*(j)) not in lines_set or\
                    (c[0]+line*(j-1),c[0]+line*(j)) not in lines_set or\
                    (c[0]+line*i+j-1,c[1]+line*i+j-1) not in lines_set:
                        break
                else:
                    count += 1
                    print 'count',count         
    return count
if __name__ == '__main__':
    # Rank 1
    assert (count_squares([1, 2], [3, 4], [1, 5], [2, 6], [4, 8], [5, 6], [6, 7],
                          [7, 8], [6, 10], [7, 11], [8, 12], [10, 11],
                          [10, 14], [12, 16], [14, 15], [15, 16]) == 3), "First, from description"
    assert (count_squares([1, 2], [2, 3], [3, 4], [1, 5], [4, 8],
                          [6, 7], [5, 9], [6, 10], [7, 11], [8, 12],
                          [9, 13], [10, 11], [12, 16], [13, 14], [14, 15],
                          [15, 16]) == 2), "Second, from description"
    assert (count_squares([1, 2], [1, 5], [2, 6], [5, 6]) == 1), "Third, one small square"
    assert (count_squares([1, 2], [1, 5], [2, 6], [5, 9], [6, 10],
                          [9, 10]) == 0), "Fourth, it's not square"
    assert (count_squares([16, 15], [16, 12], [15, 11], [11, 10],
                          [10, 14], [14, 13], [13, 9]) == 0), "Fifth, snake"

    # Rank 2
    assert (count_squares([1, 2], [2, 7], [7, 6], [6, 1], [25, 24],
                          [24, 19], [19, 20], [20, 25]) == 2), "25"
    # Rank 3
    assert (count_squares([1, 2], [2, 7], [7, 6], [6, 1], [25, 24], [24, 19], [19, 20], [20, 25],
                          [6, 11], [0, 19], [10, 0], [11, 16], [16, 21], [21, 22], [22, 23],
                          [23, 24], [20, 15], [15, 10], [10, 5],
                          [5, 4], [4, 3], [3, 2]) == 1), "With zeroes"

    print("All done? Earn rewards by using the 'Check' button!")
