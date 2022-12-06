while n:= int(input()):
    nations = []
    for _ in range(n):
        nation, *l = input().split()
        l = [*map(int, l)]
        if nation == 'Canada':
            canada = l
        else:
            nations.append(l)
    flag = False
    g = 1
    for i in range(-2, 3):
        for j in range(-2, 3):
            s = pow(100, i)
            b = pow(100, j)
            canada_score = sum(x * y for x, y in zip(canada, [g, s, b]))
            Max_score = max(p * g + q * s + r * b for p, q, r in nations)
            if canada_score >= Max_score:
                flag = True
                break
    if flag:
        print('Canada wins!')
    else:
        print('Canada cannot win.')