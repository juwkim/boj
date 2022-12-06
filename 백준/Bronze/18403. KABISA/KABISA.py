for _ in range(int(input())):
    n = [*map(int, input().split(', '))]
    for i in n:
        if i % 4 == 0:
            print(i, end=' ')