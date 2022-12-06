import sys
input = lambda: sys.stdin.readline().rstrip()

g = lambda: [*map(int, input().split())]

for cnt in range(1, 1 + int(input())):
    L, W = g()
    Map = []
    for _ in range(W):
        buf = []
        cur = 0
        for c in input():
            if c in 'GS':
                cur += 1
            else:
                cur = 0
            buf.append(cur)
        Map.append(buf)
    ans = 0
    for num in range(1, 1 + W):
        for s in range(W-num+1):
            for k in range(L):
                ans = max(ans, num * min(Map[i][k] for i in range(s, s + num)))

    print(f'Case #{cnt}: {ans}')