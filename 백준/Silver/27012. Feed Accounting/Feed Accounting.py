import sys
input = sys.stdin.readline
g = lambda: map(int, input().split())

C, F1, F2, D = g()
a = [0] * 2001
for _ in range(C):
    s, e = g()
    for i in range(s, min(e, D) + 1):
        a[i] += 1
ans = D + 1
while F1 != F2:
    ans -= 1
    F1 -= a[ans]
print(ans)