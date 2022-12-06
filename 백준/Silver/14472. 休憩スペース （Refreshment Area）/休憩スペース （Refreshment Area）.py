import sys
input = lambda: sys.stdin.readline().rstrip('\n')


g = lambda: [*map(int, input().split())]
N, M, D = g()
ans = 0
lines = []
for _ in range(N):
    line = input()
    lines.append(line)
    cur = 0
    for c in line:
        if c == '.':
            cur += 1
            if cur >= D:
                ans += 1
        else:
            cur = 0
for line in zip(*lines):
    cur = 0
    for c in line:
        if c == '.':
            cur += 1
            if cur >= D:
                ans += 1
        else:
            cur = 0
print(ans)    