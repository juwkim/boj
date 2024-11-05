def sieve(n):
    p = [1] * (n + 1)
    for i in range(2, n + 1):
        if p[i]:
            for j in range(i * i, n + 1, i):
                p[j] = 0
    return [i for i in range(2, n + 1) if p[i]]
p2 = [num * num for num in sieve(3163)]
k, a, b = map(int, open(0).read().split())
l = [1] * (b + 1)
for num in p2:
    s = (a + num - 1) // num * num
    for i in range(s, b + 1, num):
        l[i] = 0
    
while k:
    k -= l[a]
    a += 1
print(a - 1)