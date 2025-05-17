import sys
input = sys.stdin.readline

N, M = map(int, input().split())
buf = []
for _ in range(N):
    c, s, *l = input().split()
    buf.append((int(c), {(l[i], l[i + 1]) for i in range(0, len(l), 2)}))

def solve(i, credits, state):
    if credits >= M:
        return 1
    if i == N:
        return 0
    return solve(i + 1, credits, state) or state.isdisjoint(buf[i][1]) and solve(i + 1, credits + buf[i][0], state | buf[i][1])
print(("NO", "YES")[solve(0, 0, set())])