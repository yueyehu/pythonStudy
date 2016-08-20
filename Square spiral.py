def find_distance(first, second):
    i=1
    j=0
    x=y=0
    coor_dict = {}
    while i<max(first,second)+1:
        if x==-j and y == j:  
            coor_dict[i] = (x,y)
            y+=1
            j+=1
        elif -j<x<j and y==j:
            coor_dict[i] = (x,y)
            x+=1
        elif x == j and -j<y<=j:
            coor_dict[i] = (x,y)
            y-=1
        elif -j<x<=j and y == -j:
            coor_dict[i] = (x,y)
            x -= 1
        elif x == -j and -j<=y<j:
            coor_dict[i] = (x,y)
            y+=1
        i+=1
    return abs(coor_dict[first][0] - coor_dict[second][0]) + abs(coor_dict[first][1] - coor_dict[second][1])

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert find_distance(1, 9) == 2, "First"
    assert find_distance(9, 1) == 2, "Reverse First"
    assert find_distance(10, 25) == 1, "Neighbours"
    assert find_distance(5, 9) == 4, "Diagonal"
    assert find_distance(26, 31) == 5, "One row"
    assert find_distance(50, 16) == 10, "One more test"

