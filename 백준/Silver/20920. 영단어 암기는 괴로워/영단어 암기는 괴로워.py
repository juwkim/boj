from collections import defaultdict

dic = defaultdict(int)
N, M = map(int, input().split())
for _ in range(N):
    s = input()
    if len(s) >= M:
        dic[s] += 1
ans = sorted(dic, key=lambda x: (-dic[x], -len(x), x))
print(*ans)