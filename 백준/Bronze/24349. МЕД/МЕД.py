n, a, b, c = map(int, input().split())
s = [min(a , b) + (n - 2) * min(a, b, c), 0][n == 1]
print(*divmod(s, 100))