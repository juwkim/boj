N, M, K = map(int, input().split())
if K:
    a = max(min(N-2*M, K), min(M-N//2, K))
    K -= a
    if N > 2 * M:
        team = M + K//-3
    else:
        team = N//2 + (K - N%2)//-3
else:
    team = min(N//2, M)
print(team)