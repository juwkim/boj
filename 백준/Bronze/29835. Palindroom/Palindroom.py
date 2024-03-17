N = int(input())
S = list(input())
cnt = 0
for i in range(N >> 1):
    if S[i] != S[N - i - 1]:
        cnt += 1
        c = min(S[i], S[N - i - 1])
        S[i] = c
        S[N - i - 1] = c
print(cnt)
print(*S, sep='')