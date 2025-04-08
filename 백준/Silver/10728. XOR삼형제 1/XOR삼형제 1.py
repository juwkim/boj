import sys
input = sys.stdin.readline
from itertools import combinations
for _ in range(int(input())):
    N = int(input())
    def solve():
        ans = []
        for l in range(N, 0, -1):
            for p in combinations(range(1, N + 1), l):
                if all(a ^ b ^ c for a, b, c in combinations(p, 3)):
                    return p
    ans = solve()
    print(len(ans))
    print(*ans)