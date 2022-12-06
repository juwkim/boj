g=lambda:map(int,input().split())
n,m=g()
a=[*map(sum,zip(*[[*g()]for _ in[0]*n]))]
print(*sorted([*range(1,m+1)],key=lambda x:-a[x-1]))