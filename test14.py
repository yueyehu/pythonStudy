# -*- coding: cp936 -*-
'''����ֱ��ͼ������Ԫ�ظ���'''

'''�Լ��ķ���'''
def count_neighbours(grid,row,col):
    count = 0
    for i in xrange(-1,2):
        if row + i >= 0 and row + i < len(grid):
            for j in xrange(-1,2):
                if col + j >= 0 and col + j < len(grid):
                    if grid[row+i][col+j]:
                        count += 1
    return count - grid[row][col]
