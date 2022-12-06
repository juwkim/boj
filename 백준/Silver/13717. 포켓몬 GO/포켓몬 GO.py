g = lambda: [*map(int, input().split())]

name, num, cnt = '', 0, 0
for _ in range(int(input())):
    p = input()
    K, M = g()
    a = max(0, M - 2) // (K - 2)
    cnt += a
    if a > num:
        name = p
        num = a
print(cnt, name)