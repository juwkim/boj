N = int(input())
S = [*input()]
ans = 1
for i in range(1, N):
    if all(a == b for a, b in zip(S, S[i:])):
        if len(S) < i + N:
            S.extend(S[len(S) - i - N:])
        ans += 1
print(ans)