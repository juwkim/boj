g=lambda:[*map(int,input().split())]
input()
print(sum(a:=g()),sum(s-s*t for s,t in zip(a,g())))