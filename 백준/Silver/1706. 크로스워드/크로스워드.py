import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

ans = '|'
R, C = g()
buf = [input() for _ in range(R)]
for l in buf:
    for word in l.split('#'):
        if len(word) >= 2:
            ans = min(ans, word)
buf = list(map("".join, zip(*buf)))
for l in buf:
    for word in l.split('#'):
        if len(word) >= 2:
            ans = min(ans, word)
print(ans)