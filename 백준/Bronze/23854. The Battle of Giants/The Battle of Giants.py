a = int(input())
b = int(input())
if (a - b) % 3:
    print(-1)
else:
    print(a // 3, a % 3, b // 3)