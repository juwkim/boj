N, K, AS, AE, BS, BE, CS, CE = map(int, open(0).read().split())
ans, cur = "YES", 2880
for _ in range(N):
    cur = min(cur + K - 1440, AE)
    if cur < AS:
        ans = "NO"
        break
    cur = min(cur + K, BE)
    if cur < BS:
        ans = "NO"
        break
    cur = min(cur + K, CE)
    if cur < CS:
        ans = "NO"
        break
print(ans)