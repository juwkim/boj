input = __import__('sys').stdin.readline

while (s:= input().rstrip()) != "0 0 0 0":
    *l, r = s.split()
    X, Y, N = map(int, l)
    r = float(r) / 1200
    if r < 1e-9:
        if X > N * 12 * Y:
            ans = "NO"
        else:
            ans = "YES"
    else:
        if X * r > Y * (1 - 1 / pow(1 + r, 12 * N)):
            ans = "NO"
        else:
            ans = "YES"
    print(ans)