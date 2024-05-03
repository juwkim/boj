import sys
g = lambda: [*map(int, sys.stdin.readline().split())]

ans = []
N, M, K = g()
p, q = 1, 1
for X, Y in sorted([g() for _ in range(K)]) + [(N, M)]:
    if Y < q:
        print("Impossible")
        exit()
    ans.append("D" * (X - p))
    ans.append("R" * (Y - q))
    p, q = X, Y
print(*ans, sep="")