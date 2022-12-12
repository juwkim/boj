import sys
input = sys.stdin.readline
g = lambda: tuple(map(int, input().split()))

N, M = g()
rank = g()
keyword = []
for _ in range(N):
    _, *keys = g()
    keyword.append(set(keys))
for _ in range(int(input())):
    key = int(input())
    ans = [i + 1 for i in range(N) if key in keyword[i]]
    ans.sort(key=lambda x: rank[x-1])
    if ans:
        print(*ans)
    else:
        print(-1)