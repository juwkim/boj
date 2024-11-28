import sys
input = lambda: sys.stdin.readline().rstrip()

r, c = map(int, input().split())
f = 1
for i in range(r):
    p, q = divmod(c - len(s:=input()), 2)
    if q:
        if f:
            l, r = p, p + 1
        else:
            l, r = p + 1, p
        f ^= 1
    else:
        l, r = p, p
    print(f"{'.' * l}{s}{'.' * r}")