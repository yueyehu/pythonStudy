'''
Created on 2015��11��24��

@author: HKJ
'''
#golf=lambda n:reduce(lambda x,y:int(x)*(),'1'+str(n))
def golf(n,s=1):
 for i in str(n):s*=int(i) or 1#��·������˴�æ��
 return s