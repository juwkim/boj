import sys
g = lambda: [*map(int, sys.stdin.readline().split())]
from itertools import product

N, M = g()
nums = [g() for _ in range(M)]
ans = 0
state = [0] * (N + 1)
def solve(i):
    global ans
    u, v = nums[i]
    p, q = state[abs(u)], state[abs(v)]
    for a, b in product((-1, 1), repeat=2):
        if abs(u) == abs(v) and a * b < 0: continue
        if state[abs(u)] * a < 0 or state[abs(v)] * b < 0: continue
        if a * u < 0 and b * v < 0: continue
        state[abs(u)], state[abs(v)] = a, b
        if i == M - 1:
            ans = 1
            return
        else:
            solve(i + 1)
            if ans:
                return
        state[abs(u)], state[abs(v)] = p, q
solve(0)
print(ans)