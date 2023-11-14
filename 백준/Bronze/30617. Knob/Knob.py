import sys
input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

ans = 0
l1, r1 = 0, 0
for _ in range(int(input())):
    l2, r2 = g()
    ans += (l1 and l1 == l2) + (r1 and r1 == r2) + (l2 and l2 == r2)
    l1, r1 = l2, r2
print(ans)