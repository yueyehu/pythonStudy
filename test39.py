def find_route(t_s,A,B,dc,flag):
    '''
    t_s:teleports_string
    A:start
    B:end
    dc:the set of stations have been visited
    flag: 1:first call, 0: nested call
    '''
    Aset = set()
    Bset = set()
    for r in t_s:
        if A in r:Aset.add((set(r)-set(A)).pop())
        if B in r:Bset.add((set(r)-set(B)).pop())
    if len(Aset) > 0 or len(Bset) > 0:
        for a in Aset:
            for b in Bset:
                dc1 = dc.copy()
                if A + a == b + B or A + a == B + b: continue # avoid 'AB***BA' or 'AB***AB'
                if a != b and A != b and a != B and (a+b in t_s or b+a in t_s): #avoid 'ABA'
                    if len(dc) == 8 or (len(dc) == 7 and (a not in dc or b not in dc)) or (len(dc) == 6 and a not in dc and b not in dc):
                        return A + a + b + B
                t_s1 = t_s[:]
                #remove 'Aa' or 'aA' and 'bB' or 'Bb'
                try:t_s1.remove(a+A)       
                except:t_s1.remove(A+a)    
                try:t_s1.remove(b+B)      
                except:t_s1.remove(B+b)
                    
                if a == b:
                    if len(dc) >= 7:
                        return A + a + B
                    elif A != B:
                        dc1.add(a)
                        s = A + find_route(t_s1[:],a,b,dc1.copy(),0) + B
                    else:continue
                else:
                    dc1.add(a)
                    dc1.add(b)
                    s = A + find_route(t_s1[:],a,b,dc1.copy(),0) + B
                if 'X' not in s:
                    flag_t = True #mark the route right or not
                    if flag == 1:
                        for c in '12345678':
                            if c not in s:
                                flag_t = False
                                break
                    if flag_t == True:
                        return s
                    else:
                        continue  
                else:
                    continue
    return 'X'
def checkio(teleports_string):
    #return any route from 1 to 1 over all points
    t_s = teleports_string.split(',')
    return find_route(t_s[:],'1','1',set('1'),1)

#This part is using only for self-testing
if __name__ == "__main__":
    def check_solution(func, teleports_str):
        route = func(teleports_str)
        teleports_map = [tuple(sorted([int(x), int(y)])) for x, y in teleports_str.split(",")]
        if route[0] != '1' or route[-1] != '1':
            print("The path must start and end at 1")
            return False
        ch_route = route[0]
        for i in range(len(route) - 1):
            teleport = tuple(sorted([int(route[i]), int(route[i + 1])]))
            if not teleport in teleports_map:
                print("No way from {0} to {1}".format(route[i], route[i + 1]))
                return False
            teleports_map.remove(teleport)
            ch_route += route[i + 1]
        for s in range(1, 9):
            if not str(s) in ch_route:
                print("You forgot about {0}".format(s))
                return False
        return True

    assert check_solution(checkio, "12,23,34,45,56,67,78,81"), "First"
    assert check_solution(checkio, "12,28,87,71,13,14,34,35,45,46,63,65"), "Second"
    assert check_solution(checkio, "12,15,16,23,24,28,83,85,86,87,71,74,56"), "Third"
    assert check_solution(checkio, "13,14,23,25,34,35,47,56,58,76,68"), "Fourth"

