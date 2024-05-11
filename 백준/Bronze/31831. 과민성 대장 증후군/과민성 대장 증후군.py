N, M, *A = map(int, open(0).read().split())
ans, cur = 0, 0
for a in A:
    cur = max(0, cur + a)
    ans += cur >= M
print(ans)