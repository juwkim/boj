from itertools import combinations
N = int(input())
names = [input() for _ in range(N)]

def sol(a, b):
    for i in range(1, min(len(a), len(b)) + 1):
        if a[-i:] == b[:i]:
            return 1
    return 0

ans = 0
for a, b in combinations(names, 2):
    ans += sol(a, b) or sol(b, a)
print(ans)