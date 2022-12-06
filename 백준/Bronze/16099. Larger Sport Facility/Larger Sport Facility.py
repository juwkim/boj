for _ in range(int(input())):
    a, b, c, d = map(int, input().split())
    s = a * b
    t = c * d
    print(["Tie", "TelecomParisTech", "Eurecom"][(s > t) - (s < t)])