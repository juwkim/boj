n, k, s, x = map(int, input().split())

ans = -1
cur = s - x
for i in range(n):
    if cur % n:
        cur += k
        continue
    ans = i
    break
print(ans)