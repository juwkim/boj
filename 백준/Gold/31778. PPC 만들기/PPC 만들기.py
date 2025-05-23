N, K = map(int, input().split())
S = list(input())
j = N - 1
for i in range(N):
    if S[i] == 'C':
        while j > i and S[j] == 'C':
            j -= 1
        if j <= i:
            break
        S[i], S[j] = S[j], S[i]
        j -= 1
        K -= 1
        if K == 0:
            break
ans, P = 0, 0
for i in range(N):
    if S[i] == 'P':
        P += 1
    elif S[i] == 'C':
        ans += P * (P - 1)
print(ans >> 1)