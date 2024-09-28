import sys
input = sys.stdin.readline

N = int(input())
x, y = zip(*[map(int, input().split()) for _ in range(N)])
def solve(l):
    l = sorted(l)
    ans = sum(l[i] - l[0] for i in range(1, N))
    cur = ans
    for i in range(1, N):
        cur += (l[i] - l[i - 1]) * (2 * i - N)
        ans = min(ans, cur)
    return ans
print(solve(x) + solve(y))