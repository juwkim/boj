g = lambda: [*map(int, input().split())]

n = int(input())
if n < 4:
    print(0)
else:
    a = [0] + g()
    j = 2
    for i in range(3, n-1):
        if a[i] - a[i - 1] < a[j] - a[j - 1]:
            j = i
    print(a[n-1] - a[0] + a[j] - a[j-1])
    print(n, j, j + 1, 1)