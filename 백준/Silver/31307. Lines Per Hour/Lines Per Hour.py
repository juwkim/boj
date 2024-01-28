import sys
input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

n, lph = g()
cnt = 5 * lph
ans = 0
for num in sorted(int(input()) for _ in range(n)):
    cnt -= num
    if cnt < 0:
        break
    ans += 1
print(ans)