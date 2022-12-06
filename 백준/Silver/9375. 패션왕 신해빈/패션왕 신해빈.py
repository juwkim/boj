for _ in range(int(input())):
    check = {}
    for _ in range(int(input())):
        name = input().split()[1]
        try:
            check[name] += 1
        except:
            check[name] = 1
    count = 1
    for i in check.values():
        count *= i + 1
    print(count - 1)