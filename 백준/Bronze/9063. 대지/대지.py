l=[*map(int,open(0).read().split())]
g=lambda x:max(x)-min(x)
print(g(l[1::2])*g(l[2::2]))