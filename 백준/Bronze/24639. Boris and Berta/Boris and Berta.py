g = lambda: [*map(int, input().split())]

n, m, c = map(int, [input() for _ in range(3)])

diff = 1e9
ans = None
for i in range(n//m + 2):
    num = n - m * i
    if num > 0:
        j = num // c
        
        if abs(num - j * c) < diff:
            ans = i, j
            diff = abs(num - j * c)

        if abs(num - (j + 1) * c) < diff:
            ans = i, j + 1
            diff = abs(num - (j + 1) * c)
    elif abs(num) < diff:
        ans = i, 0
        diff = abs(num)
print(*ans)