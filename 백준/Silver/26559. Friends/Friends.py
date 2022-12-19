for _ in range(int(input())):
    dic = {}
    for _ in range(int(input())):
        name, num = input().split()
        dic[name] = int(num)
    print(', '.join(sorted(dic, key=lambda x: - dic[x])))