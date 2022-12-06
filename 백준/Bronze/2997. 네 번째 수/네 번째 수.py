a, b, c = sorted(map(int, input().split()))
if c - b == b - a:
    print(2 * c-b)
elif c - b > b - a:
    print((b + c) // 2)
else:
    print((a + b) // 2)