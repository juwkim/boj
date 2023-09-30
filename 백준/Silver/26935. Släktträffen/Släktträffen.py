import sys
input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

N, M = g()
P = [0] + g()
L = [0]
for i in range(1, N + 1):
    d, cur = 1, i
    while P[cur]:
        cur = P[cur]
        d += 1
    L.append(d)

ans, *nums = g()
for num in nums:
    if ans == num:
        continue
    ans, num = sorted([ans, num], key=lambda x: L[x])
    while L[num] != L[ans]:
        num = P[num]
    while num != ans:
        num, ans = P[num], P[ans]
print(ans)