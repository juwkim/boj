import sys
input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

N = int(input())
ans, h = None, float("-inf")
for num in g():
    if num >= N:
        t = num
    else:
        q, r = divmod(N, num)
        if r <= num - r:
            t = num * q
        else:
            t = num * (q + 1)
    if abs(N - t) < abs(N - h):
        ans, h = num, t
print(ans, h)
