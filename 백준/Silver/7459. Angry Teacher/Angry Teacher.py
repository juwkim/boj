import sys
input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

n, l, k, m = g()
a = [int(input()) for _ in range(n + 1)]
for c in range(l, l + k):
    p = a[0]
    for i in range(1, n + 1):
        p = p * c + a[i]
    ans = sum(num * num for num in map(int, str(p)[-m:]))
    print(ans)