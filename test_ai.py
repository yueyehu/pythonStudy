from heapq import heappush, heappop
def Dijkstra(graph, start):
    A = [None] * len(graph)
    queue = [(0, start)]
    while queue:
        path_len, v = heappop(queue)
        if A[v] is None: # v is unvisited
            A[v] = path_len
            for w, edge_len in graph[v].items():
                if A[w] is None:
                    heappush(queue, (path_len + edge_len, w))            
    return [0 if x is None else x for x in A]

from math import floor
def through_block(A,B):
    '''
    find the blocks' coordinates between A and B
    '''
    C = set()
    ###
    if A[0] == B[0]:
        for i in range(min(A[1],B[1])+1,max(A[1],B[1])):
            C.add((A[0],i))
        return C
    if A[1] == B[1]:
        for i in range(min(A[0],B[0])+1,max(A[0],B[0])):
            C.add((i,A[1]))
        return C
    ###
    c = 1.0*(abs(A[1] - B[1]) + 1)/(abs(A[0] - B[0]) + 1)
    xs = (B[0]-A[0])/abs(B[0]-A[0])
    ys = (B[1]-A[1])/abs(B[1]-A[1])
    xd = 1 if xs == -1 else 0
    yd = 1 if ys == 1 else 0
    
    for i in range(abs(A[0]-B[0])):
        a = A[0] + xs*(i+xd)
        b = A[1]+c*ys*(i+1)-yd
        C.add((int(floor(a)),int(floor(b)+1)))
        C.add((int(floor(a))+1,int(floor(b)+1)))
        if abs(floor(b) - b) < 0.0000001:
            C.add((int(floor(a)),int(floor(b))))
            C.add((int(floor(a))+1,int(floor(b))))
       
    ###
    c = 1.0*(abs(A[0] - B[0]) + 1)/(abs(A[1] - B[1]) + 1)
    xs = (B[0]-A[0])/abs(B[0]-A[0])
    ys = (B[1]-A[1])/abs(B[1]-A[1])
    xd = 1 if xs == 1 else 0
    yd = 1 if ys == -1 else 0
    
    for i in range(abs(A[1]-B[1])):
        b = A[1] + ys*(i+yd)
        a = A[0]+c*xs*(i+1)-xd
        C.add((int(floor(a)+1),int(floor(b))))
        C.add((int(floor(a)+1),int(floor(b)+1)))
        if abs(floor(a) - a) < 0.0000001:
            C.add((int(floor(a)),int(floor(b))))
            C.add((int(floor(a)),int(floor(b)+1)))
    ###
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
        for j,c in enumerate(s):
            if c == 'B':
                    b_count += 1
                    b_list[i][j] = b_count
                    b_cor[b_count] = (i,j)
            elif c == '-': b_list[i][j] = -1
            elif c == 'W': b_list[i][j] = -2
            elif c == 'A':
                b_list[i][j] = 0
                b_cor[0] = (i,j)
    b_dict = {i:{} for i in range(b_count+1)}
    
    for cor_i in b_cor:
        for cor_j in b_cor:
            if cor_i != cor_j:
                cor_t = through_block(b_cor[cor_i],b_cor[cor_j])
                cor_t_flag = False
                for b in cor_t:
                    if b_list[b[0]][b[1]] == -2:
                        cor_t_flag = True
                        break
                if cor_t_flag == False:
                        b_dict[cor_i][cor_j] = ((b_cor[cor_i][0] - b_cor[cor_j][0])**2 + (b_cor[cor_i][1] - b_cor[cor_j][1])**2)**0.5
                        b_dict[cor_j][cor_i] = ((b_cor[cor_i][0] - b_cor[cor_j][0])**2 + (b_cor[cor_i][1] - b_cor[cor_j][1])**2)**0.5
                              
    shortest_route = Dijkstra(b_dict,0)
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

