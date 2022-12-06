while n:= int(input()):
    dic = {}
    for _ in range(n):
        y, _, m = input().split()
        if dic.get(y):
            dic[y][0] += 1
            if m == 'Gold':
                dic[y][1] += 1
        else:
            if m == 'Gold':
                dic[y] = [1, 1]
            else:
                dic[y] = [1, 0]
    a = min(dic, key=lambda x: (-dic[x][1], x))
    b = min(dic, key=lambda x: (-dic[x][0], x))
    print(a, b)