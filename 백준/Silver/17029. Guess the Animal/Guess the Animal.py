import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

N = int(input())
l = []
for _ in range(N):
    name, K, *characteristic = input().split()
    l.append(set(characteristic))
ans = 0
for i in range(N - 1):
    for j in range(i + 1, N):
        ans = max(ans, len(l[i] & l[j]))
print(ans + 1)