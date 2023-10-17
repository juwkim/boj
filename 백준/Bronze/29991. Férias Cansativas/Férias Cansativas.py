import sys
input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

D, C, R = g()
a = [int(input()) for _ in range(C)]
cur = D + sum(int(input()) for _ in range(R))
ans = R
for num in a:
    if num <= cur:
        cur -= num
        ans += 1
    else:
        break
print(ans)