g = lambda: [*map(int, input().split())]

n, k, x, y = g()
q = int(input())
k_sum = x + y * (k - 1)
one_floor = (n // k) * k_sum + (n % k) * y
for num in g():
    a, b = divmod((num - 1) % one_floor, k_sum)
    ans = a * k + b // x + 1
    print(ans)