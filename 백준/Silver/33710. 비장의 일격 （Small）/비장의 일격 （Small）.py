from string import ascii_uppercase
from itertools import combinations

N, K = map(int, input().split())
S = input()
ans = N
def solve(txt, num):
    global ans
    ans = min(ans, len(txt))
    if num == 0:
        return
    for c in ascii_uppercase:
        if c == 'X': continue
        idx = [i for i in range(len(txt)) if txt[i] == c]
        for a, b in combinations(idx, 2):
            solve(txt[:a] + txt[b+1:], num - 1)

solve(S, K)
print(ans)