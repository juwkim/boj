x = input()
l = len(x)
k = int(x)
if int(input()):
    for i in range(10):
        num = x[0] + str(i) * (l - 1)
        if int(num) >= k:
            break
    if num == x[0] * l:
        num = int(num)
        while num % 10 and num > k:
            num -= 1
        print(num)
    else:
        print(num)
else:
    num = x[0] * l
    if int(num) >= k:
        print(num)
    elif x[0] <= '8':
        num = str(int(x[0]) + 1) * l
        print(num)
    else:
        num = '1' * (l + 1)
        print(num)