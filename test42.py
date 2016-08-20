from heapq import heappush, heappop
def Dijkstra(graph, start):
    A = [None] * len(graph)
    queue = [(0, start)]
    while queue:
        path_len, v = heappop(queue)
        print path_len, v,queue
        if A[v] is None: # v is unvisited
            A[v] = path_len
            for w, edge_len in graph[v].items():
                if A[w] is None:
                    heappush(queue, (path_len + edge_len, w))

    # to give same result as original, assign zero distance to unreachable vertices             
    return [0 if x is None else x for x in A]

from math import floor
def through_block(A,B):
    C = set()
    if A[0] == B[0]:
        if A[1] > B[1]:
            for i in range(B[1]+1,A[1]):
                C.add((A[0],i))
        else:
            for i in range(A[1]+1,B[1]):
                C.add((A[0],i))
        return C
    if A[1] == B[1]:
        if A[0] > B[0]:
            for i in range(B[0]+1,A[0]):
                C.add((i,A[1]))
        else:
            for i in range(A[0]+1,B[0]):
                C.add((i,A[1]))
        return C
    
    c = 1.0*(abs(A[1] - B[1]) + 1)/(abs(A[0] - B[0]) + 1)
    xs = (B[0]-A[0])/abs(B[0]-A[0])
    ys = (B[1]-A[1])/abs(B[1]-A[1])
    xd = 1 if xs == -1 else 0
    yd = 1 if ys == 1 else 0
    
    for i in range(abs(A[0]-B[0])):
        a = A[0] + xs*(i+xd)
        b = A[1]+c*ys*(i+1)-yd
        
        if floor(b) != b: 
            C.add((int(floor(a)),int(floor(b)+1)))
            C.add((int(floor(a))+1,int(floor(b)+1)))
        else:
            C.add((int(floor(a)),int(floor(b))))
            C.add((int(floor(a)),int(floor(b)+1)))
            C.add((int(floor(a)+1),int(floor(b))))
            C.add((int(floor(a)+1),int(floor(b)+1)))
    

    c = 1.0*(abs(A[0] - B[0]) + 1)/(abs(A[1] - B[1]) + 1)
    xs = (B[0]-A[0])/abs(B[0]-A[0])
    ys = (B[1]-A[1])/abs(B[1]-A[1])
    xd = 1 if xs == 1 else 0
    yd = 1 if ys == -1 else 0
    
    for i in range(abs(A[1]-B[1])):
        b = A[1] + ys*(i+yd)
        a = A[0]+c*xs*(i+1)-xd
        
        if floor(a) != a: 
            C.add((int(floor(a)+1),int(floor(b))))
            C.add((int(floor(a)+1),int(floor(b)+1)))
        else:
            C.add((int(floor(a)),int(floor(b))))
            C.add((int(floor(a)),int(floor(b)+1)))
            C.add((int(floor(a)+1),int(floor(b))))
            C.add((int(floor(a)+1),int(floor(b)+1)))
    

    C.add(B)
    C.add(A)
    C.remove(B)
    C.remove(A)
   
    return C

def checkio(bunker):
    if bunker[0][0] == 'A':return 0
    b_list = [[0]*len(bunker[0]) for i in range(len(bunker))]
    b_cor = dict()
    b_count = 0
    for i,s in enumerate(bunker):
        #print 's',s
        for j,c in enumerate(s):
            #print 'c',c
            if c == 'B':
                    b_count += 1
                    b_list[i][j] = b_count
                    b_cor[b_count] = (i,j)
            elif c == '-': b_list[i][j] = -1
            elif c == 'W': b_list[i][j] = -2
            elif c == 'A':
                b_list[i][j] = 0
                b_cor[0] = (i,j)
    print 'b_list',b_list
    print 'b_cor',b_cor
    b_dict = {i:{} for i in range(b_count+1)}
    for cor_i in b_cor:
        for cor_j in b_cor:
            if cor_i != cor_j:
                print cor_i,cor_j,b_cor[cor_i],b_cor[cor_j]
                cor_t = through_block(b_cor[cor_i],b_cor[cor_j])
                print 'cor_t',cor_t
                cor_t_flag = False
                for b in cor_t:
                    print b
                    if b_list[b[0]][b[1]] == -2:
                        cor_t_flag = True
                        break
                if cor_t_flag == False:
                        b_dict[cor_i][cor_j] = ((b_cor[cor_i][0] - b_cor[cor_j][0])**2 + (b_cor[cor_i][1] - b_cor[cor_j][1])**2)**0.5
                        b_dict[cor_j][cor_i] = ((b_cor[cor_i][0] - b_cor[cor_j][0])**2 + (b_cor[cor_i][1] - b_cor[cor_j][1])**2)**0.5
                
    print 'b_dict',b_dict               
    shortest_route = Dijkstra(b_dict,0)
    print 'shortest_route',shortest_route
    return round(shortest_route[1],2)

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    def almost_equal(checked, correct, significant_digits=2):
        precision = 0.1 ** significant_digits
        return correct - precision < checked < correct + precision

    assert almost_equal(checkio([
        "B--",
        "---",
        "--A"]), 2.83), "1st example"
    assert almost_equal(checkio([
        "B-B",
        "BW-",
        "-BA"]), 4), "2nd example"
    assert almost_equal(checkio([
        "BWB--B",
        "-W-WW-",
        "B-BWAB"]), 12), "3rd example"
    assert almost_equal(checkio([
        "B---B-",
        "-WWW-B",
        "-WA--B",
        "-W-B--",
        "-WWW-B",
        "B-BWB-"]), 9.24), "4th example"

