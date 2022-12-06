def solve(start):

    res = 2500
    for size in range(N - start + 1, 0, -1):
        if palin[start][size]:
            res = min(res, dp[start + size] + 1)
    dp[start] = res
    return


txt = input()
N = len(txt)
palin = [[1, 1] + [0 for _ in range(N-1)] for _ in range(N+1)]
dp = [0 for _ in range(N+2)]

for size in range(2, N+1):
    for start in range(1, N - size + 2):
        if palin[start+1][size-2] and txt[start-1] == txt[start+size-2]:
            palin[start][size] = 1

for i in range(N, 0, -1):
    solve(i)
print(dp[1])