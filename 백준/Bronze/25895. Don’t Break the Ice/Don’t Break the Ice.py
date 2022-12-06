for i in range(1, 1 + int(input())):
    n, cnt = map(int, input().split())
    r, c = bytearray(n + 1), bytearray(n + 1)
    ans = 0
    for _ in range(cnt):
        a, b = map(int, input().split())
        ans += (r[a] + c[b] == 2)
        r[a], c[b] = 1, 1
    print(f'Strategy #{i}: {ans}\n')