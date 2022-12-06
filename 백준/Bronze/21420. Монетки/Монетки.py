N = int(input())
S = sum(int(input()) for _ in range(N))
print(min(S, N - S))