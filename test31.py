def break_rings(rings):
    rings_d = dict()
    for ring_con in rings:
        con = [str(x) for x in ring_con]
        try:
            rings_d[con[0]].add(con[1])
        except:
            rings_d[con[0]] = set()
            rings_d[con[0]].add(con[01])
        try:
            rings_d[con[1]].add(con[0])
        except:
            rings_d[con[1]] = set()
            rings_d[con[1]].add(con[0])
    count = 0
    while rings_d != {}:
        min_con = 0
        for k in rings_d:
            if min_con != 0:
                 if len(rings_d[min_con]) > len(rings_d[k]): min_con = k
            else:
                min_con = k
        remove_d = rings_d[min_con].copy()
        for r in remove_d:
            for k in rings_d[r]:
                rings_d[k].remove(r)
            rings_d.pop(r)
            count += 1
        remove_d = []
        for k in rings_d:
            if len(rings_d[k]) == 0: remove_d.append(k)
        for k in remove_d:
            rings_d.pop(k)
                
    return count

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert break_rings(({1, 2}, {2, 3}, {3, 4}, {4, 5}, {5, 6}, {4, 6})) == 3, "example"
    assert break_rings(({1, 2}, {1, 3}, {1, 4}, {2, 3}, {2, 4}, {3, 4})) == 3, "All to all"
    assert break_rings(({5, 6}, {4, 5}, {3, 4}, {3, 2}, {2, 1}, {1, 6})) == 3, "Chain"
    assert break_rings(({8, 9}, {1, 9}, {1, 2}, {2, 3}, {3, 4}, {4, 5}, {5, 6}, {6, 7}, {8, 7})) == 5, "Long chain"


