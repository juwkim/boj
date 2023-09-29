import sys
input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

o, a, b = g()
ans = 0
for i in range(1, (o - b) // a + 1):
    if (o - i * a) % b == 0:
        ans = 1
        break
print(ans)