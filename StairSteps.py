'''
Created on 2015/11/28

@author: HKJ
'''
def golf(n):
    if len(n)==0:return 0
    return max(n[0]+golf(n[1:]),(golf(n[2:])+n[1])if len(n)>=2 else 0)
if __name__ == '__main__':
     # These "asserts" using only for self-checking and not necessary for auto-testing
     assert golf((5, -3, -1, 2)) == 6
     assert golf((5, 6, -10, -7, 4)) == 8
     assert golf((-11, 69, 77, -51, 23, 67, 35, 27, -25, 95)) == 393
     assert golf((-21, -23, -69, -67, 1, 41, 97, 49, 27)) == 125
     print("Use 'Check' to earn sweet rewards!")
