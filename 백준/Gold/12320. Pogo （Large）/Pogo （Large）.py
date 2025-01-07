for tc in range(1, 1 + int(input())):
    x, y = map(int, input().split())
    Sum, dist = 0, abs(x) + abs(y)
    n = 0
    while Sum < dist or Sum - dist & 1:
        n += 1
        Sum += n
    ans = []
    for i in range(n, 0, -1):
        if abs(x) > abs(y):
            if x > 0:
                ans.append("E")
                x -= i
            else:
                ans.append("W")
                x += i
        else:
            if y > 0:
                ans.append("N")
                y -= i
            else:
                ans.append("S")
                y += i
    print(f"Case #{tc}: {''.join(ans[::-1])}")