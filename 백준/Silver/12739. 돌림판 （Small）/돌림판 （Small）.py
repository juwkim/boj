import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

from collections import Counter

N, K = g()
S = input()
for _ in range(K):
    new = ['' for _ in range(N)]
    for i in range(N):
        l = "".join(sorted([S[i - 1], S[i], S[(i + 1) % N]]))
        if l in ("BBB", "GGG", "RRR", "BGR"):
            new[i] = 'B'
        elif l in ("GRR", "BGG", "BBR"):
            new[i] = 'R'
        else:
            new[i] = 'G'
    S = new
cnt = Counter(S)
print(cnt['R'], cnt['G'], cnt['B'])