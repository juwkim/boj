g = lambda: [*map(int, input().split())]
N = int(input())
if N == 2:
    print(1, 1)
else:
    a, b = g(), g()
    x = a[1] + a[2] - b[2] >> 1
    print(x, end=' ')
    for num in a[1:]:
        print(num - x, end=' ')