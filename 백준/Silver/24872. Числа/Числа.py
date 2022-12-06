x = input()
l = len(x)
k = int(x)
if int(input()):
    ans = None
    for i in range(10):
        if x[0] == str(i):
            for j in range(1, l):
                for a in range(10):
                    num = x[0] * j + str(a) + x[0] * (l - j - 1)
                    if int(num) >= k:
                        if ans == None:
                            ans = int(num)
                        else:
                            ans = min(ans, int(num))
        else:
            num = x[0] + str(i) * (l - 1)
            if int(num) >= k:
                if ans == None:
                    ans = int(num)
                else:
                    ans = min(ans, int(num))
    print(ans)
else:
    num = x[0] * l
    if int(num) >= k:        print(num)
    elif x[0] <= '8':
        num = str(int(x[0]) + 1) * l
        print(num)
    else:
        num = '1' * (l + 1)
        print(num)