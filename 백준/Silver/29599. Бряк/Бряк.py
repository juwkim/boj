import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

buf = [[]]
n = int(input())
for _ in range(n):
    v, c = g()
    buf.append([v, v * c])
for _ in range(int(input())):
    a, b, k = g()
    gram = k / buf[a][0] * buf[a][1]
    buf[a][0] -= k
    buf[b][0] += k
    buf[a][1] -= gram
    buf[b][1] += gram

print(n)
for i in range(1, n + 1):
    v, vc = buf[i]
    print(v, vc / v if v else 0)