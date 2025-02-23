def solve():
    s, d, m = input(), int(input(), 2), input()
    if len(m) >= d and len(s) >= d:
        print("Infinite money!")
        return
    s, m = int(s, 2), int(m, 2)
    day = 0
    while m:
        day += 1
        m >>= 1
        if day % d == 0:
            m += s
    num = []
    while True:
        day, r = divmod(day, 2)
        num.append(r)
        if day == 0:
            break
    print(*num[::-1], sep='')
solve()