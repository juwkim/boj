n = int(input())
if n < 7:
    print((1, 2, 6, 24, 12, 72)[n - 1])
else:
    num = 504
    for i in range(8, n + 1):
        num *= i
        while num % 10 == 0:
            num //= 10
        num %= 1000000000000
    print(str(num)[-3:])