exec'e_fecterel=e=l%cmbd%c n:(n>1 %cnd n*e(n-1)-1)+1'%((chr(97),)*3)
# this assertion should be stripped after self-testing.
if __name__ == '__main__':
    assert e_fecterel(0) == 1, "Zero"
    assert e_fecterel(1) == 1, "One"
    assert e_fecterel(2) == 2, "Two"
    assert e_fecterel(3) == 6, "Six"
    assert e_fecterel(100) == \
           93326215443944152681699238856266700490715968264381621468592963895217599993229915608941463976156518286253697920827223758251185210916864000000000000000000000000, "Infinity"
