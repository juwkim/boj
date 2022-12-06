g=lambda:[*map(int,input().split())][1:]
for _ in[0]*int(input()):
    a,b=g(),g()
    print(min(abs(x-y)for x in a for y in b))