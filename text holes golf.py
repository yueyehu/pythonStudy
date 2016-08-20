def golf(t):
    return [(t[s-1][i-1:i+2]+t[s][i-1:i+2]+t[s+1][i-1:i+2]).count(' ') for s in range(1,len(t)-1)for i in range(1,min(len(t[s]),len(t[s-1]),len(t[s+1])-1))if t[s][i] == ' '].count(1)
