def golf(n):  
    return (p for p in (x for x in xrange(n,98998)if str(x)[:] == str(x)[::-1])if 0 not in [p%d for d in xrange(2,n-1)]).next()
