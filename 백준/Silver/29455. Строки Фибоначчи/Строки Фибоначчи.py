k = int(input())
if k < 5:
    print((1, 1, 1, 3, 4)[k])
else:
    a, b = 3, 5
    num = 6
    for _ in range(k - 5):
        num += b
        a, b = b, a + b
    print(num)