# -*- coding: cp936 -*-
import random as ri
def gamble(): 
    print '''*********��ӭ�����Ĵ�С********* 
����[1]����� [0]����С [quit]�˳�\n'''
 
    
 
    yourchoice = ''
 
    done    = False
 
    while not done:
 
        dice = lambda : ri.randint(1,6)
 
        x,y,z = dice(),dice(),dice()
 
        yourchoice = input('�����С��[1/0]?')
 
        if yourchoice in [0,1]:
 
            rs = 1 and (x+y+z)>=9 or 0
 
            print '''Binggo! ����A[%d],����B[%d],����C[%d],���̽��%d
 
ע�����(tou)���� ''' % (x,y,z,x+y+z)
 
            tmp = "��" if yourchoice else"С"
 
            print '�������[',tmp,']'
 
            if yourchoice == rs:
 
                print 'Ӯ!'
 
            else :
 
                print '��!'
 
        goahead = raw_input( '�Ƿ����? [y]')
 
        done = False if goahead == 'y' else True
 
    else:
 
        print "��ӭ����...\n�˳���Ϸ"
 
        return 1
