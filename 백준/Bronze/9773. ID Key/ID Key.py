for _ in range(int(input())):
    S = input()
    num1 = sum(int(i) for i in S)
    num2 = int(S[-3:]) * 10
    ans = num1 + num2
    if ans < 1000:
        ans += 1000
    print("%04d" % (ans % 10000))