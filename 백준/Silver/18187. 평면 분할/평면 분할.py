N = int(input())
ans = 1
for i in range(N):
    q, r = divmod(i, 3)
    ans += 2 * q + r + 1
print(ans)