import sys
input = lambda: sys.stdin.readline().rstrip()

a, b = set(), set()
S, E, Q = input().split()
while True:
    try:
        t, name = input().split()
        if t <= S:
            a.add(name)
        elif E <= t <= Q:
            b.add(name)
    except:
        break
print(len(a & b))