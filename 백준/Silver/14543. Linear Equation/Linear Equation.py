for tc in range(1, int(input()) + 1):
    a, _, b, _, c = input().split()
    a, b, c = map(int, (a[:-1], b, c))
    print(f"Equation {tc}")
    if a:
        if b == c:
            ans = "0.000000"
        else:
            sign = "-" if c < b else ""
            ip, rem = divmod(abs(c - b), a)
            frac6 = (rem * 10**6) // a
            ans = f"{sign}{ip}.{frac6:06d}"
        print(f"x = {ans}")
    elif b == c:
        print("More than one solution.")
    else:
        print("No solution.")
    print()