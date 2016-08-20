'''
Created on 2015/11/23

@author: HKJ
'''
def is_skew_symmetric(matrix):
    if len(matrix) != len(matrix[0]):
        return False
    for i in range(len(matrix)):
        for j in range(len(matrix)/2+1):
            if (i == j and matrix[i][i] != 0) or (i!=j and matrix[i][j] != -matrix[j][i]):
                return False
    return True
                
                
            


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert is_skew_symmetric([
        [0, 1, 2],
        [-1, 0, 1],
        [-2, -1, 0]]), "1st example"
    assert not is_skew_symmetric([
        [0, 1, 2],
        [-1, 1, 1],
        [-2, -1, 0]]), "2nd example"
    assert not is_skew_symmetric([
        [0, 1, 2],
        [-1, 0, 1],
        [-3, -1, 0]]), "3rd example"

    print("All set? Click 'Check' to review your code and earn rewards!")