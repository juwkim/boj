import sys
input = lambda: sys.stdin.readline().rstrip()

R = int(input())
abacus = [[*map(int, input().split())] for _ in range(R)][::-1]
base = [1]
for i in range(R - 1):
    base.append(base[i] * (sum(abacus[i]) + 1))
num = (sum(base[i] * abacus[i][0] for i in range(R)) + int(input())) % (base[-1] * (sum(abacus[-1]) + 1))
ans = [[0, 0] for _ in range(R)]
for i in range(R - 1):
    r = num % base[i + 1] // base[i]
    num -= r * base[i]
    ans[i][0], ans[i][1] = r, sum(abacus[i]) - r
q = num // base[-1]
ans[-1][0], ans[-1][1] = q, sum(abacus[-1]) - q
for l in reversed(ans):
    print(*l)