a = sorted(map(int, input()), reverse=True)
if a[-1] == 0 and sum(a) % 3 == 0:
    print(*a, sep="")
else:
    print(-1)