'''
Created on 2016/1/17/

@author: HKJ
'''
FONT = ("--X--XXX-XXX-X-X-XXX--XX-XXX-XXX--XX-XX--",
        "-XX----X---X-X-X-X---X-----X-X-X-X-X-X-X-",
        "--X---XX--X--XXX-XX--XXX--X--XXX-XXX-X-X-",
        "--X--X-----X---X---X-X-X-X---X-X---X-X-X-",
        "--X--XXX-XXX---X-XX---XX-X---XXX-XX---XX-")


def recognize(image):
    flag = True
    for i in range(5):
        if image[i][0] != 0:
            flag = False
            break
    if flag == False:
        image = image[:][1::]
    i = 0
    s = 0
    while i<len(image[0])-2:
        s=s*10+findNum([[image[k][j] for j in range(i+1,i+4)]for k in range(0,5)])
        i += 4
    #print s
    return s
def findNum(img):
    #print img
    for i in range(10):
        error_c = 0
        for j in range(1,4):
            for k in range(5):
                r = 1 if FONT[k][i*4+j] == 'X' else 0
                if img[k][j-1] != r:
                    error_c += 1
                if error_c > 1:
                    break
            if error_c > 1:
                break
        if error_c <= 1:
            return (i+1)%10
    return 0
    
if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert recognize([[0, 1, 1, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0],
                    [0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
                    [0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0],
                    [0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0],
                    [0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0]]) == 394, "394 clear"
    assert recognize([[0, 1, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 0],
                    [0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
                    [0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0],
                    [0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0],
                    [0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0]]) == 394, "again 394 but with noise"

    print("Earn cool rewards by using the 'Check' button!")
