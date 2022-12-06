g = lambda: [*map(int, input().split())]


dp = [[[None for _ in range(21)] for _ in range(21)] for _ in range(21)]

def solve(a, b, c):
    if all(0 <= num <= 20 for num in (a, b, c)) and dp[a][b][c] != None:
        return dp[a][b][c]
    
    if a <= 0 or b <= 0 or c <= 0:
        dp[0][0][0] = 1
        return 1
    
    if a > 20 or b > 20 or c > 20:
        dp[20][20][20] = solve(20, 20, 20)
        return dp[20][20][20]
    
    if a < b and b < c:
        dp[a][b][c-1] = solve(a, b, c-1)
        dp[a][b-1][c-1] = solve(a, b-1, c-1)
        dp[a][b-1][c] = solve(a, b-1, c)
        
        return dp[a][b][c-1] + dp[a][b-1][c-1] - dp[a][b-1][c]
    
    dp[a-1][b][c] = solve(a-1, b, c)
    dp[a-1][b-1][c] = solve(a-1, b-1, c)
    dp[a-1][b][c-1] = solve(a-1, b, c-1)
    dp[a-1][b-1][c-1] = solve(a-1, b-1, c-1)
    
    return dp[a-1][b][c] + dp[a-1][b-1][c] + dp[a-1][b][c-1] - dp[a-1][b-1][c-1]


while (l:= g()) != [-1, -1, -1]:
    a, b, c = l
    ans = solve(a, b, c)    
    print(f'w({a}, {b}, {c}) = {ans}')