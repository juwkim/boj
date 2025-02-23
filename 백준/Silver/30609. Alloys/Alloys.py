import sys
input = sys.stdin.readline

n = int(input())
l = []
for _ in range(n):
    id, a, b = input().split()
    l.append((float(a), float(b), id))
p, m = [], 0
for a, b, id in sorted(l, reverse=True):
    if b >= m:
        m = b
        p.append(id)
print(*sorted(p))