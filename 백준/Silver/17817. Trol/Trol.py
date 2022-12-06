g = lambda: [*map(int, input().split())]

for _ in range(int(input())):
    a, b = g()
    r, q = divmod(b - a, 9)
    cnt = b - a + 1 + r * 36
    for num in range(a + 9 * r - 1, b):
        cnt += num % 9
    print(cnt)