from bisect import bisect_right
res = [1, 1]
a, b = res
for _ in range(99998):
    res.append(res[-2] + res[-1])

for _ in range(int(input())):
    n = int(input())
    print(bisect_right(res, n))