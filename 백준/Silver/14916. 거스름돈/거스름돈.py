n = int(input())
if n in [1, 3]:
    print(-1)
else:
    cnt, q = divmod(n, 5)
    cnt += [0, 2, 1, 3, 2][q]
    print(cnt)