for _ in range(int(input())):
    dic = {"(shirt)": [], "(pants)": [], "(socks)": []}
    for _ in range(int(input())):
        *name, l = input().split()
        dic[l].append(" ".join(name))
    while True:
        try:
            print(dic["(shirt)"].pop(), dic["(pants)"].pop(), dic["(socks)"].pop(), sep=', ')
        except:
            break
    print()