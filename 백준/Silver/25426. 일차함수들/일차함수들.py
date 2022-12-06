import sys
input = lambda: sys.stdin.readline().rstrip()

g = lambda: [*map(int, input().split())]


ans = 0
buf = []
N = int(input())
for _ in range(N):
    a, b = g()
    ans += b
    buf.append(a)
buf.sort()
ans += sum((i+1) * buf[i] for i in range(N))
print(ans)