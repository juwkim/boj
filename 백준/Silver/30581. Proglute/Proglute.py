N = int(input())
m = 10**9 + 7
ans = (N * pow(2, N - 3, m)) % m
print(ans)