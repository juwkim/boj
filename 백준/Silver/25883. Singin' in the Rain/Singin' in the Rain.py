g = lambda: [*map(int, input().split())]

for _ in range(int(input())):
    ans = 0
    t, s = g()
    cur, *tracks = g()
    cur += 1
    for song in tracks:
        ans += min((cur - song) % t, (song - cur) % t)
        cur = song + 1
    print(ans)