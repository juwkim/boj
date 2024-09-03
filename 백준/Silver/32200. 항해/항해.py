ans, left = 0, 0
N, X, Y = map(int, input().split())
for A in map(int, input().split()):
    q, r = divmod(A, X)
    ans += q
    left += max(0, r - (Y - X) * q)
print(ans)
print(left)