input()
n=[*map(int,input().split())]
i=n.index(max(n))
print(sum(n[:i]),sum(n[i+1:]))