for _ in range(int(input())):
    print(int(str(sum(map(lambda x: int(x[::-1]), input().split())))[::-1]))