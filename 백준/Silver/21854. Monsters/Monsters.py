n, *k = map(int, open(0).read().split())
ans, m = 0, 1000000007
for num in k:
    ans = (ans + pow(2, num, m)) % 1000000007
print(ans)