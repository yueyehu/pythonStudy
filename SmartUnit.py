'''
Created on 2015/11/23

@author HKJ
'''
from battle import commander
unit_client = commander.Client()

commandCenter     = unit_client.ask_center()
towerDefence      = dict()
harmlessBuildings = dict()

dangerMap  = dict()
attackPath = list()

def InitDangerMap():
    global dangerMap
    for i in range(20,41):
        for j in range(0,41):
            dangerMap[(i,j)] = 0
            
def JudgeCircle(center,radius):
    domain = list()
    for i in range(center[0]-radius,center[0]+radius+1):
        if i >= 20 and i <=40: 
            for j in range(center[1]-radius,center[1]+radius+1):
                if j >=0 and j <= 40:
                    if min(abs(i-center[0]),abs(i-center[0]+1))**2 + min(abs(j-center[1]),abs(j-center[1]+1))**2 < radius**2:
                        domain.append((i,j))
    return domain

def UpdateDangerMap(domain,dangerDegree,flag=True):
    for d in domain:
        if d in dangerMap:
            dangerMap[d] += (1 if flag else -1)*dangerDegree

def MainLoop():
    global towerDefence
    global dangerMap
    global attackPath
    towers = unit_client.ask_towers()
    for t in towers:
        towerDefence[t['id']] = dict()
        towerDefence[t['id']]['rate_of_fire']    = t['rate_of_fire']
        towerDefence[t['id']]['damage_per_shot'] = t['damage_per_shot']
        towerDefence[t['id']]['firing_range']    = t['firing_range']
        towerDefence[t['id']]['coordinates']     = t['coordinates']
        domain = JudgeCircle(t['coordinates'],t['firing_range'])
        UpdateDangerMap(domain,t['rate_of_fire']*t['damage_per_shot'])
        
                                       
if __name__ == '__main__':
    InitDangerMap()
    domain = JudgeCircle([22,15],12)
    UpdateDangerMap(domain,6,True)
    print dangerMap


