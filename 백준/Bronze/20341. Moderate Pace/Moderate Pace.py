input()
for a in zip(*[[*map(int,input().split())]for _ in[0]*3]):
    print(sorted(a)[1],end=' ')