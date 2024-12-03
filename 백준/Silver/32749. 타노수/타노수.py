N, T = map(int, input().split())
X = input()
l = 2 ** (N - T)
print(max(X[i:i+l] for i in range(0, len(X), l)))