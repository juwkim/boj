from bisect import bisect_left

res = [0, 1]
a, b = res
while b <= 10**9:
    a, b = b, a + b
    res.append(b)

for _ in range(int(input())):
    temp = []
    n = int(input())
    idx = bisect_left(res, n)
    while n:
        if res[idx] <= n:
            temp.append(res[idx])
            n -= res[idx]
            idx -= 2
        else:
            idx -= 1
    print(*temp[::-1])