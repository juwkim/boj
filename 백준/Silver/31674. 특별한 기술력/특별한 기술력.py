N, *l = map(int, open(0).read().split())
ans, cnt = 0, 1
for H in sorted(l):
    ans = (ans + H * cnt) % 1000000007
    cnt = (cnt << 1) % 1000000007
print(ans)