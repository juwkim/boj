import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

for _ in range(int(input())):
    m, n, k = g()
    Map = [bytearray(n) for _ in range(m)]
    for _ in range(k):
        x, y = g()
        Map[x-1][y-1] = True
    ans = sum(sum(len(l) >= 2 for l in line.split(b'\x01')) for line in Map)
    ans += sum(sum(len(l) >= 2 for l in bytearray(line).split(b'\x01')) for line in zip(*Map))
    print(ans)