nums = [2, 4, 5, 7, 8, 10, 11, 13]
alpha = "0123456789ACDEFHJKLMNPRTVWX"
dic = {alpha[i]: i for i in range(27)}
for i in range(int(input())):
    n, num = input().split()
    for k, v in {'B': '8', 'G': 'C', 'I': '1', 'O': '0', 'Q': '0', 'S': '5', 'U': 'V', 'Y': 'V', 'Z': '2'}.items():
        num = num.replace(k, v)
    check = sum(dic[D] * num for D, num in zip(num[:-1], nums)) % 27
    if num[8] == alpha[check]:
        ans = 0
        mul = 1
        for i in range(7, -1, -1):
            ans += mul * dic[num[i]]
            mul *= 27
        print(n, ans)
    else:
        print(n, "Invalid")