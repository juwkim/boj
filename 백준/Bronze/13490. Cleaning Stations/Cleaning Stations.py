g = lambda: [*map(int, input().split())]

for cnt in range(1, 1 + int(input())):
    n, m = g()
    nums = g()
    buf = []
    for _ in range(n):
        buf.append(sum(i * j for i, j in zip(nums, g())))
    Max = max(buf)
    res = [i+1 for i in range(n) if buf[i] == Max]
    print(f'Data Set {cnt}:')
    for num in res:
        print(num)
    print()