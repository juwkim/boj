for _ in range(int(input())):
    print(max([input().split() for _ in range(int(input()))], key=lambda x: int(x[1]))[0])