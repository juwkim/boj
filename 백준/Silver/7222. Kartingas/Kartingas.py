import sys
input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

N, K = g()
pos = [0]
for num in sorted(g()):
    if num >= K:
        break
    pos.append(num)
pos.append(K)
ans = max(b - a for a, b in zip(pos, pos[1:]))
print(ans)