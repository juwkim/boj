from functools import*
print(int(reduce(lambda s,t:s+t[0]+t[1],zip(*map(lambda s:bin(int(s))[2:].zfill(16),input().split())),''),2))