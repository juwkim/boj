A, B, K, M = map(int, input().split())

ans = 0
for num in range(10 ** (K - 1), 10 ** K):
    s = str(num)
    cur = num
    i = 0
    while cur <= B:
        if A <= cur <= B and cur % M == 0:
            ans += 1
        cur = cur * 10 + int(s[i])
        i = (i + 1) % len(s)
print(ans)