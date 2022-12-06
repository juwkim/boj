while (s:= input()) != '0 0 0 0':
    a, b, c, d = map(int, s.split())
    ans = 120 + (a - b) % 40 + (c - b) % 40 + (c - d) % 40
    print(ans * 9)