import sys
input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

a, b = g()
R = int(input())
Map = [bytearray(R) for _ in range(R)]
ans = 0
while True:
    if Map[a][b]:
        break
    Map[a][b] = 1
    ans += 1
    if a + b + 2 < R:
        a, b = a + 1, b + 1
    else:
        a, b = a // 2, b // 2
print(ans)