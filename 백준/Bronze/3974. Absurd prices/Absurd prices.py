def get_absurdity(c):
    c = c.rstrip('0')
    d = int(c[-1])
    a = len(c) - (d == 5)
    return 2 * a - (d != 5)

for _ in range(int(input())):
    c = int(input().rstrip('0'))
    absurdity = get_absurdity(str(c))
    d = c % 10
    p, q, r = c - d, c + 10 - d, c + 5 - d
    if 0.95 * c <= p <= 1.05 * c and get_absurdity(str(p)) < absurdity:
        ans = "absurd"
    elif 0.95 * c <= q <= 1.05 * c and get_absurdity(str(q)) < absurdity:
        ans = "absurd"
    elif d != 5 and 0.95 * c <= r <= 1.05 * c and get_absurdity(str(c + 5 - d)) < absurdity:
        ans = "absurd"
    else:
        ans = "not absurd"
    print(ans)