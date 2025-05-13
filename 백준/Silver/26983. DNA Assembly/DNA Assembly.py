from itertools import permutations

def merge(a, b):
    min_len = min(len(a), len(b))
    for l in range(min_len, 0, -1):
        if a[-l:] == b[:l]:
            return a + b[l:]
    return a + b

N = int(input())
ans = 1e9
for p in permutations(input() for _ in range(N)):
    cur = p[0]
    for i in range(1, N):
        cur = merge(cur, p[i])
    ans = min(ans, len(cur))
print(ans)