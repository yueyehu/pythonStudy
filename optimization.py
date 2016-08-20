# -*- coding: cp936 -*-
import time
import random
import math

people = [('Seymour','BOS'),('Franny','DAL'),('Zooey','CAK'),('Walt','MIA'),('Buddy','ORD'),('Les','OMA')]
# New York的LaGuardia机场
destination='LGA'
flights={}
# 
for line in file('schedule.txt'):
    origin,dest,depart,arrive,price=line.strip().split(',')
    flights.setdefault((origin,dest),[])
      # 将航班详情添加到航班列表中
    flights[(origin,dest)].append((depart,arrive,int(price)))


def hillclimb(domain,costf):
    # 创建一个随机解
    sol=[random.randint(domain[i][0],domain[i][1])for i in range(len(domain))]

    # 主循环
    while 1:
        # 创建相邻解的列表
        neighbors=[]
        for j in range(len(domain)):
            # 在每个方向上相对于原值偏离一点
            if sol[j]>domain[j][0]:
                neighbors.append(sol[0:j]+[sol[j]-1]+sol[j+1:])
            if sol[j]<domain[j][1]:
                neighbors.append(sol[0:j]+[sol[j]+1]+sol[j+1:])
        # 在相邻解中寻找最优解
        current=costf(sol)
        best=current
        for j in range(len(neighbors)):
            cost=costf(neighbors[j])
        if cost<best:
            best=cost
            sol=neighbors[j]

        # 如果没有更好的解，则退出循环
        if best==current:
            break
    return sol


def randomoptimize(domain,costf):
    best=999999999
    bestr=None
    for i in range(1000):
        # 创建一个随机解
        r=[random.randint(domain[i][0],domain[i][1])for i in range(len(domain))]

        # 得到成本
        cost=costf(r)

        # 与到目前为止的最优解进行比较
        if cost<best:
            best=cost
            bestr=r 
    return r


