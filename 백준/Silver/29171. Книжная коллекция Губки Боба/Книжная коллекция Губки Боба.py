import sys
input = sys.stdin.readline

n = int(input())
pos = list(range(0, 2 * n + 1))
cnt = n
f = lambda x: x <= n and pos[x] <= n
for _ in range(int(input())):
    i, j = map(int, input().split())
    t = f(i) + f(j)
    pos[i], pos[j] = pos[j], pos[i]
    print(cnt:= cnt + f(i) + f(j) - t)