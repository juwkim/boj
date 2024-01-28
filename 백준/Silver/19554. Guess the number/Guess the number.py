l, r = 1, int(input())
while True:
    m = (l + r) >> 1
    print(f"? {m}", flush=True)
    s = int(input())
    if s == 0:
        print(f"= {m}")
        break
    elif s == 1:
        r = m - 1
    else:
        l = m + 1