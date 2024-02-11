input()
i=0
for l in map(len,input().split('R')):print(*range(i+l+1,i,-1));i+=l+1