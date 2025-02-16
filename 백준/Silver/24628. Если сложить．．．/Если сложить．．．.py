from math import log2

n, *a = map(int, open(0).read().split())
ans = 0
for num in a:
    cur = num
    for i in range(int(log2(num)), 1, -1):
        j = int(num ** (1 / i) + 1e-9)
        if j ** i == num:
            cur = j
            break
    ans += cur
print(ans)