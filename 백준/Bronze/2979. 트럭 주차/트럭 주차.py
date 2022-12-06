from functools import reduce
A, B, C = map(int, input().split())
time = [0]*101
for _ in range(3):
    s, e = map(int, input().split())
    for i in range(s, e):
        time[i] += 1
price = reduce(lambda x, y: x + [0, A, B, C][y] * y, time, 0)
print(price)