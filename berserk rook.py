def berserk_rook(berserker, enemies):
    e_count = 0
    e_eat = 0
    if len(enemies) == 0:return 0

    print  berserker,enemies
    for e in enemies:
        if berserker[0] == e[0] or berserker[1] == e[1]:
            e_eat = 1
            enset = enemies.copy()
            enset.remove(e)
            flag = True
            for c in enset:
                if berserker[0] == e[0] == c[0] and  (berserker[1] < c[1] < e[1] or berserker[1] > c[1] > e[1]):
                    flag = False
                    break
                elif berserker[1] == e[1] == c[1] and  (berserker[0] < c[0] < e[0] or berserker[0] > c[0] > e[0]):
                    flag = False
                    break
            if flag == False: continue
            e_temp = berserk_rook(e,enset)
            if e_count < e_temp:e_count = e_temp
    return e_eat + e_count
'''
if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert berserk_rook(u'd3', {u'd6', u'b6', u'c8', u'g4', u'b8', u'g6'}) == 5, "one path"
    assert berserk_rook(u'a2', {u'f6', u'f2', u'a6', u'f8', u'h8', u'h6'}) == 6, "several paths"
    assert berserk_rook(u'a2', {u'f6', u'f8', u'f2', u'a6', u'h6'}) == 4, "Don't jump through"
'''
