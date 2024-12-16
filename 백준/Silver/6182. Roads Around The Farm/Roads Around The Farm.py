N, K = map(int, input().split())
def solve(i):
    if i < K + 2 or (i - K) & 1:
        return 1
    return solve((i - K) // 2) + solve((i + K) // 2)
print(solve(N))