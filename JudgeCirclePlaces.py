'''
Created on 2015/11/23/

@author: HKJ
'''
def JudgeCicle(center,radius):
    domain = list()
    for i in range(center[0]-radius,center[0]+radius+1):
        if i >= 20 and i <=40: 
            for j in range(center[1]-radius,center[1]+radius+1):
                if j >=0 and j <= 40:
                    if min(abs(i-center[0]),abs(i-center[0]+1))**2 + min(abs(j-center[1]),abs(j-center[1]+1))**2 < radius**2:
                        domain.append([i,j])
    return domain
        
if __name__ == '__main__':
    print JudgeCicle([23,3],3)