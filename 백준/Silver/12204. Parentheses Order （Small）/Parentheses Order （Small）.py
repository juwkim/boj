def g(): return [*map(int, input().split())]

def generate_parenthesis(n, k):

    N, opened = 2 * n, 0
    res = []
    for N in range(2 * n, 0, -1):
        if opened < 0:
            break
        if opened == n or dp[N - 1][opened + 1] == 0:
            res.append(")")
            opened -= 1
        elif opened == 0 or dp[N - 1][opened - 1] == 0:
            res.append("(")
            opened += 1
        elif k <= dp[N-1][opened + 1]:
            res.append("(")
            opened += 1
        else:
            res.append(")")
            k -= dp[N-1][opened + 1]
            opened -= 1

    # For valid strings k should be 1
    if k == 1:
        return ''.join(res)
    else:
        return "Doesn't Exist!"

MAX = 10
dp = [[0] * (2 * MAX + 2) for _ in range(2 * MAX + 1)]
dp[0][0] = 1
for i in range(1, 2 * MAX + 1):
    for j in range(i + 1):
        dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]

for t in range(1, 1 + int(input())):
    n, k = map(int, input().split())
    ans = generate_parenthesis(n, k)
    print(f'Case #{t}: {ans}')