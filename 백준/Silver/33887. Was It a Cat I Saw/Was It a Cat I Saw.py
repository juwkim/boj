from itertools import product

for _ in range(int(input())):
    X = int(input())
    b = bin(X)[2:]
    if b == b[::-1]:
        print(0)
        continue
    l = X.bit_length()
    ans = X + 1 - (1 << l - 1)
    for p in map(''.join, product('01', repeat=l//2 - 1)):
        if l & 1:
            num1 = int('1' + p + '0' + p[::-1] + '1', 2)
            num2 = int('1' + p + '1' + p[::-1] + '1', 2)
            ans = min(ans, abs(X - num1), abs(X - num2))
        else:
            num = int('1' + p + p[::-1] + '1', 2)
            ans = min(ans, abs(X - num))
    print(ans)