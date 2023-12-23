import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

N = int(input())
nums = g()

a = [*range(N, 0, -1)]
for i in range(1, N):
    b = a[N-1:N-1-i:-1] + a[:N-i]
    for j in range(1, N):
        c = b[N-1:N-1-j:-1] + b[:N-j]
        for k in range(1, N):
            d = c[N-1:N-1-k:-1] + c[:N-k]
            if d == nums:
                print(i, j, k)
                exit()