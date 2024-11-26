def solve(l):
    ans, Sum = 0, 0
    for i in range(min(N, K)):
        ans = max(ans, Sum + l[i] * (K - i))
        Sum += l[i]
    return ans

N, K, *A = map(int, open(0).read().split())
print(max(solve(A), solve(A[::-1])))