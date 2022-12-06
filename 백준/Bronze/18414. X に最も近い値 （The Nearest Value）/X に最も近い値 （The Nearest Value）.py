X, L, R = map(int, input().split())
print(L if X < L else R if X > R else X)