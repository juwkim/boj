import sys
input = lambda: sys.stdin.readline().rstrip()
MOD = 10**9 + 7

def solve():
    N = len(W)
    v = [i for i in range(1, N - 3) if W[i:i+3] == "kot"]
    M = len(v)
    if M == 0:
        return 1
    prev = [-1] * M
    j = 0
    for i in range(M):
        while j < i and v[j] <= v[i] - 4:
            j += 1
        if j and v[j - 1] <= v[i] - 4:
            prev[i] = j - 1
    total, total_prev = 0, 1
    dp0 = [0] * M
    dp1 = [0] * M
    for i in range(M):
        dp0[i] = total_prev
        if prev[i] >= 0:
            ways = dp0[prev[i]] + dp1[prev[i]]
        else:
            ways = 1
        dp1[i] = ways % MOD
        total = (dp0[i] + dp1[i]) % MOD
        total_prev = total
    return total % MOD

for _ in range(int(input())):
    W = input()
    print(solve())