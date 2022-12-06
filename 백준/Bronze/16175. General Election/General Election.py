g=lambda:map(int,input().split())
for _ in [0]*int(input()):
    _,M=g()
    a=[*map(sum,zip(*[[*g()]for _ in [0]*M]))]
    print(a.index(max(a))+1)