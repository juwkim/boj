import sys
input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

N, M = g()
buf = [input() for _ in range(N)]
for line in buf:
    ans = [len(i) for i in line.split('.') if i]
    if ans:
        print(*ans)
    else:
        print(0)
for line in map(''.join, zip(*buf)):
    ans = [len(i) for i in line.split('.') if i]
    if ans:
        print(*ans)
    else:
        print(0)