N = int(input())
S = input()
ans = sum(S[i] != S[N-1-i] for i in range(N//2))
print(ans)