n = int(input())
if n < 7:
    print(0)
else:
    num = n * (n + 1) >> 1
    if num & 1:
        num -= 1
    print(num)