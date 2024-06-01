alpha = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
idx = {alpha[i]: i for i in range(36)}
k, n = map(int, input().split())
m = input()
digit_sum = sum(idx[c] for c in m)
ans = "Impossible"
for a in range(int(m, k) + 1, k**n):
    num = 0
    b = []
    while a:
        a, r = divmod(a, k)
        num += r
        b.append(alpha[r])
    if num == digit_sum:
        ans = "".join(b[::-1])
        break
print(ans)