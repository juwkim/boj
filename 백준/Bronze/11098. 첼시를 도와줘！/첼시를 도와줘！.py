for _ in range(int(input())):
    s = [input().split() for _ in range(int(input()))]
    print(max(s, key=lambda x: int(x[0]))[1])