a1, a2, a3, a4 = sorted(int(input()) for _ in range(4))
b = int(input())
if a1 == a4 or a1 + b == a2 == a3 == a4:
    print(1)
else:
    print(0)