import sys
input = sys.stdin.readline

N = int(input())
P = [[*map(int, input().split())] for _ in range(N)]
X, Y = zip(*P)

def dist(l):
    l = sorted(l)
    d = sum(l[i] - l[0] for i in range(1, N))
    dic = {l[0]: d}
    for i in range(1, N):
        d += (l[i] - l[i - 1]) * (2 * i - N)
        dic[l[i]] = d    
    return dic

X_dist, Y_dist = dist(X), dist(Y)
ans = min(P, key=lambda x: (X_dist[x[0]] + Y_dist[x[1]], x))
print(*ans)