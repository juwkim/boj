a, b, c = sorted(map(int, input().split()))
if a + b == c:
    print(1)
elif a * b == c:
    print(2)
else:
    print(3)