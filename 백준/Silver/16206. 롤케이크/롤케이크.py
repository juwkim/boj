N, M, *A = map(int, open(0).read().split())
ans = 0
for num in sorted(A, key=lambda x: (x % 10, x)):
    if num < 10:
        continue
    if num == 10:
        ans += 1
    elif M:
        q, r = divmod(num, 10)
        if r or M < q - 1:
            cnt = min(M, q)
            ans += cnt
            M -= cnt
        else:
            ans += q
            M -= q - 1
print(ans)