# -*- coding: cp936 -*-
import time
import random
import math

people = [('Seymour','BOS'),('Franny','DAL'),('Zooey','CAK'),('Walt','MIA'),('Buddy','ORD'),('Les','OMA')]
# New York��LaGuardia����
destination='LGA'
flights={}
# 
for line in file('schedule.txt'):
    origin,dest,depart,arrive,price=line.strip().split(',')
    flights.setdefault((origin,dest),[])
      # ������������ӵ������б���
    flights[(origin,dest)].append((depart,arrive,int(price)))


def hillclimb(domain,costf):
    # ����һ�������
    sol=[random.randint(domain[i][0],domain[i][1])for i in range(len(domain))]

    # ��ѭ��
    while 1:
        # �������ڽ���б�
        neighbors=[]
        for j in range(len(domain)):
            # ��ÿ�������������ԭֵƫ��һ��
            if sol[j]>domain[j][0]:
                neighbors.append(sol[0:j]+[sol[j]-1]+sol[j+1:])
            if sol[j]<domain[j][1]:
                neighbors.append(sol[0:j]+[sol[j]+1]+sol[j+1:])
        # �����ڽ���Ѱ�����Ž�
        current=costf(sol)
        best=current
        for j in range(len(neighbors)):
            cost=costf(neighbors[j])
        if cost<best:
            best=cost
            sol=neighbors[j]

        # ���û�и��õĽ⣬���˳�ѭ��
        if best==current:
            break
    return sol


def randomoptimize(domain,costf):
    best=999999999
    bestr=None
    for i in range(1000):
        # ����һ�������
        r=[random.randint(domain[i][0],domain[i][1])for i in range(len(domain))]

        # �õ��ɱ�
        cost=costf(r)

        # �뵽ĿǰΪֹ�����Ž���бȽ�
        if cost<best:
            best=cost
            bestr=r 
    return r


