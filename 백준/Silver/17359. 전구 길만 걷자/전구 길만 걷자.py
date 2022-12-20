from itertools import permutations
N = int(input())
buf = [input() for _ in range(N)]
ans = sum(sum(a != b for a, b in zip(s, s[1:])) for s in buf)

diff = 1e9
for l in permutations(buf, N):
    diff = min(diff, sum(a[-1] != b[0] for a, b in zip(l, l[1:])))
print(ans + diff)