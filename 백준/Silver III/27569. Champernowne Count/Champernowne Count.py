n, k = map(int, input().split())
ans, num = 0, 0
for i in range(1, n + 1):
    l = len(str(i))
    num = (num * 10 ** l + i) % k
    if num == 0:
        ans += 1
print(ans)