def sieve(num):
    prime = [True] * (num + 1)
    prime[0], prime[1] = False, False
    for i in range(2, int(num ** 0.5) + 1):
        if prime[i]:
            for j in range(i * i, num + 1, i):
                prime[j] = False
    return prime

T, *nums = map(int, open(0))
n = max(nums)
p = sieve(n)

a = [0] * (n + 1)
a[1], a[2] = 1, 1
for i in range(3, n + 1):
    if p[i]:
        a[i] = a[i - 2] + 1
    else:
        a[i] = a[i - 1] + 1
for num in nums:
    print(a[num])