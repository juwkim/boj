input()
c=1e9
print(*[c:=min(c+1,int(n))for n in input().split()])