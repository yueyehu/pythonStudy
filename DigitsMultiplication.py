'''
Created on 2015年11月24日

@author: HKJ
'''
#golf=lambda n:reduce(lambda x,y:int(x)*(),'1'+str(n))
def golf(n,s=1):
 for i in str(n):s*=int(i) or 1#短路计算帮了大忙了
 return s