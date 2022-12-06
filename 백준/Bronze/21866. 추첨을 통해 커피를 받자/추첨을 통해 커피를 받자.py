n=[*map(int,input().split())]
print(['none','draw','hacker'][any(n[i]>100*(i//2+1)for i in range(9))+(sum(n)>=100)])