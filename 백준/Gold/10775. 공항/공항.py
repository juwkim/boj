import sys
input = lambda: sys.stdin.readline().rstrip()

G = int(input())
P = int(input())
parent = [*range(G + 1)]

def find(x):
    ret = x
    while ret != parent[ret]:
        ret = parent[ret]
    parent[x] = ret
    return ret

ans = 0
for _ in range(P):
    x = find(int(input()))
    if x == 0:
        break
    parent[x] = parent[x - 1]
    ans += 1
print(ans)