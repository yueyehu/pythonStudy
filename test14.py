# -*- coding: cp936 -*-
'''计算直方图的相邻元素个数'''

'''自己的方法'''
def count_neighbours(grid,row,col):
    count = 0
    for i in xrange(-1,2):
        if row + i >= 0 and row + i < len(grid):
            for j in xrange(-1,2):
                if col + j >= 0 and col + j < len(grid):
                    if grid[row+i][col+j]:
                        count += 1
    return count - grid[row][col]
