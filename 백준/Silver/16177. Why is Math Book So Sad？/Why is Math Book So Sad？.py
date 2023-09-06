while True:
    try:
        A, B, C, D = map(int, input().split())
        ans = None
        for x in range(pow(2, 16)):
            y = x * x - D
            if y < 0:
                continue
            if (x + y) ** B + y != C:
                continue
            z = A - (x * x + y * y)
            if z < 0:
                continue
            ans = x, y, z
            break
        if ans is None:
            print("No solution")
        else:
            print(*ans)
    except Exception as e:
        print(e)
        break