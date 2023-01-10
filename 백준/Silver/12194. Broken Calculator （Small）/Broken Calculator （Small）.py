def g(): return [*map(int, input().split())]

for t in range(1, 1 + int(input())):
    nums = g()
    X = int(input())
    dp = [1e9] * (max(10, X) + 1)
    for i in range(10):
        if nums[i]:
            dp[i] = 1

    if dp[X] != 1e9:
        ans = 2
    else:
        for i in range(4, 1 + X):
            if all(dp[int(digit)] == 1 for digit in str(i)):
                dp[i] = len(str(i))
            else:
                for j in range(2, int(i ** .5) + 1):
                    q, r = divmod(i, j)
                    if r:
                        continue
                    dp[i] = min(dp[i], dp[q] + dp[j] + 1)
        if dp[X] == 1e9:
            ans = 'Impossible'
        else:
            ans = dp[X] + 1        
    print(f'Case #{t}: {ans}')