import sys
input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

N, K = g()
cnt = 0
for expire_day in sorted(int(input()) for _ in range(N)):
    day = cnt // K + 1
    if day <= expire_day:
        cnt += 1
print(cnt)