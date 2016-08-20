def checkio(matrix):
    count = 0
    for i,r in enumerate(matrix):
        for j,d in enumerate(r):
            count = 0
            for k in range(3):
                try:
                    if matrix[i][j+k+1] == d:
                        count += 1
                except:
                    break
            if count >= 3:
                print i,j,count,'1'
                return True
            count = 0
            for k in range(3):
                try:
                    if matrix[i+k+1][j] == d:
                        count += 1
                except:
                    break
            if count >= 3:
                print i,j,count,'2'
                return True

            count = 0
            for k in range(3):
                try:
                    if matrix[i+k+1][j+k+1] == d:
                        count += 1
                except:
                    break
            if count >= 3:
                print i,j,count,'3'
                return True

            count = 0
            for k in range(3):
                try:
                    if matrix[i+k+1][j-k-1] == d:
                        count += 1
                except:
                    break
            if count >= 3:
                print i,j,count,'4'
                return True
    return False

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        [1, 2, 1, 1],
        [1, 1, 4, 1],
        [1, 3, 1, 6],
        [1, 7, 2, 5]
    ]) == True, "Vertical"
    assert checkio([
        [7, 1, 4, 1],
        [1, 2, 5, 2],
        [3, 4, 1, 3],
        [1, 1, 8, 1]
    ]) == False, "Nothing here"
    assert checkio([
        [2, 1, 1, 6, 1],
        [1, 3, 2, 1, 1],
        [4, 1, 1, 3, 1],
        [5, 5, 5, 5, 5],
        [1, 1, 3, 1, 1]
    ]) == True, "Long Horizontal"
    assert checkio([
        [7, 1, 1, 8, 1, 1],
        [1, 1, 7, 3, 1, 5],
        [2, 3, 1, 2, 5, 1],
        [1, 1, 1, 5, 1, 4],
        [4, 6, 5, 1, 3, 1],
        [1, 1, 9, 1, 2, 1]
    ]) == True, "Diagonal"
