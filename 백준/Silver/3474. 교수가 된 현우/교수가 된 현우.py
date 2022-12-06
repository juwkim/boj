_, *l = map(int, open(0).read().split())
for N in l:
    ans, div = 0, 5
    while True:
        r = N // div
        ans += r
        div *= 5
        if r == 0:
            break
    print(ans)