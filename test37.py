# -*- coding: cp936 -*-
import random as ri
def gamble(): 
    print '''*********欢迎来到赌大小********* 
输入[1]代表大 [0]代表小 [quit]退出\n'''
 
    
 
    yourchoice = ''
 
    done    = False
 
    while not done:
 
        dice = lambda : ri.randint(1,6)
 
        x,y,z = dice(),dice(),dice()
 
        yourchoice = input('买入大小盘[1/0]?')
 
        if yourchoice in [0,1]:
 
            rs = 1 and (x+y+z)>=9 or 0
 
            print '''Binggo! 骰子A[%d],骰子B[%d],骰子C[%d],买盘结果%d
 
注意读作(tou)骰子 ''' % (x,y,z,x+y+z)
 
            tmp = "大" if yourchoice else"小"
 
            print '您买的是[',tmp,']'
 
            if yourchoice == rs:
 
                print '赢!'
 
            else :
 
                print '输!'
 
        goahead = raw_input( '是否继续? [y]')
 
        done = False if goahead == 'y' else True
 
    else:
 
        print "欢迎再来...\n退出游戏"
 
        return 1
