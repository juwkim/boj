for _ in range(int(input())):
    s = input()
    dic = [input() for _ in range(int(input()))]
    print(min(dic, key=lambda x: sum(i != j for i, j in zip(s, x))))