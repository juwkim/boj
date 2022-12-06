g = lambda: [*map(int, input().split())]

for _ in range(int(input())):
    n, m, p, q, t = g()
    
    a, b = t // p, t // q
    num1, num2 = (n - 1) // a, (m - 1) // b
    x, y = n - a * num1, m - b * num2
    if x * p + y * q <= t:
        print(num1 + num2 + 1)
    else:
        print(num1 + num2 + 2)