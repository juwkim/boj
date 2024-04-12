import sys
input = sys.stdin.readline

n, m = map(int, input().split())
l = [[i, 0] for i in range(1, n + 1)]
for _ in range(m):
    k = int(input())
    if k & 1:
        l[k // 2][1] ^= 1
    for i in range(k // 2):
        j = k - i - 1
        l[i][1] ^= 1
        l[j][1] ^= 1
        l[i], l[j] = l[j], l[i]
ans = {}
for i in range(n):
    num, d = l[i]
    ans[num] = f"{'+-'[d]}{i + 1}"
for _ in range(int(input())):
    print(ans[int(input())])