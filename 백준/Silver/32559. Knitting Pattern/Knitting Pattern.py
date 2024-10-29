N, P = map(int, input().split())
r = (N - P) // 2 % P
if P == 2 * r:
    ans = 0
else:
    ans = 2 * r
print(ans)