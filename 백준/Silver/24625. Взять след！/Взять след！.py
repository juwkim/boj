n = int(input())
a = sorted([int(input()) for _ in range(n)], reverse=True)

k = 1
while (k + 1) * (k + 1) <= n:
    k += 1
while k > 1 and a[k - 1] <= 0:
    k -= 1
print(sum(a[:k]))