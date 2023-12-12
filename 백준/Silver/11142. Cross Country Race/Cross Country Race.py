import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

for _ in range(int(input())):
    N, S = g()
    V = g()
    ans = 0
    while V:
        ans += 1
        t = [S / num + i for i, num in enumerate(V)]
        tmp = []
        for i in range(len(t)):
            if any(t[j] >= t[i] for j in range(i)):
                tmp.append(V[i])
        V = tmp
    print(ans)