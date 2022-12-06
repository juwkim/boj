from bisect import bisect_left
g = lambda: [*map(int, input().split())]

buf = []
for i in range(1, 9000):
    val = 1
    start = 9000
    while start >= 1:
        val *= start
        start -= i
    key = len(str(val))
    buf.append(key)
buf = buf[::-1]

for i in range(1, 1 + int(input())):
    num = 9000 - bisect_left(buf, int(input()))
    if num == 9000:
        print(f'Case #{i}: ...')
    else:
        print(f"Case #{i}: IT'S OVER 9000" + '!' * num)