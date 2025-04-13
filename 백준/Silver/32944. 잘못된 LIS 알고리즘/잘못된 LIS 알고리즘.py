N, M, K = map(int, input().split())
if M == N:
    print(-1)
else:
    ans = [*range(1, K)]
    ans.append(N)
    ans.extend(range(N - 1, N - 1 - (N - 1 - M), -1))
    ans.extend(range(K, N - 1 - (N - 1 - M) + 1))
    print(*ans)