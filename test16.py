# -*- coding: cp936 -*-
'''判断＃字游戏胜负'''

'''自己的方法'''
def checkio(game_result):
    d = {'X':False,'O':False}
    for i in xrange(3):
        if game_result[i][0] == game_result[i][1] == game_result[i][2]:
            d[game_result[i][0]] = True
        if game_result[0][i] == game_result[1][i] == game_result[2][i]:
            d[game_result[0][i]] = True
    if game_result[0][0] == game_result[1][1] == game_result[2][2]:
        d[game_result[0][0]] = True
    if game_result[0][2] == game_result[1][1] == game_result[2][0]:
        d[game_result[0][2]] = True
    
    if d['X'] == d['O']:
        return 'D'
    elif d['X']:
        return 'X'
    else:
        return 'O'
