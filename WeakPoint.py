'''
Created on 2015/11/23/

@author: HKJ
'''
#golf=lambda m:[[sum(r)for r in m].index(min([sum(r)for r in m]))for m in [m,map(list,zip(*m))]]
golf=lambda m:[[sum(r)for r in m].index(min([sum(r)for r in m]))for m in [m,[[k[n]for k in m]for n in range(len(m[0]))]]]
if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert golf([[7, 2, 7, 2, 8],
                  [2, 9, 4, 1, 7],
                  [3, 8, 6, 2, 4],
                  [2, 5, 2, 9, 1],
                  [6, 6, 5, 4, 5]]) == [3, 3]
    assert golf([[7, 2, 4, 2, 8],
                  [2, 8, 1, 1, 7],
                  [3, 8, 6, 2, 4],
                  [2, 5, 2, 9, 1],
                  [6, 6, 5, 4, 5]]) == [1, 2]
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
