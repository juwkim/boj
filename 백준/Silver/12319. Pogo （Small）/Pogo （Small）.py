for tc in range(1, 1 + int(input())):
    x, y = map(int, input().split())
    ans = ""
    if x > 0: ans = "WE" * x
    elif x < 0: ans = "EW" * -x
    if y > 0: ans += "SN" * y
    elif y < 0: ans += "NS" * -y
    print(f"Case #{tc}: {ans}")