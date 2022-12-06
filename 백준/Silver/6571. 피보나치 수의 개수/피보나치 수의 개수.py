from bisect import bisect_left, bisect_right

res = [1, 2]
a, b = 1, 2
while b <= 10**100:
    a, b = b, a + b
    res.append(b)

while (s := input()) != '0 0':
    a, b = map(int, s.split())
    print(bisect_right(res, b) - bisect_left(res, a))