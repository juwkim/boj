import sys
input = sys.stdin.readline
from math import comb

def solve(N, M, K):
    return sum(comb(M, i) * comb(N - M, M - i) for i in range(K, M + 1)) / comb(N, M)

for _ in range(int(input())):
    nums = [solve(*map(int, input().split())) for _ in range(int(input()))]
    num = max(nums)
    ans = [i + 1 for i, n in enumerate(nums) if n == num]
    print(*ans)