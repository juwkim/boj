input()
p=[*map(int,input().split())]
a,b=sorted(p)[-2:]
print(*[x-(b,a)[x==b]for x in p])