def solve():
    a = input()[::-1]
    if a[0] != 'O' or "OO" in a:
        return "INVALID"
    l = 16
    while True:
        n = l
        for c in a:
            if c == 'E':
                n <<= 1
            else:
                n, r = divmod(n - 1, 3)
                if r or n & (n - 1) == 0:
                    break
        else:
            return n
        l <<= 1
print(solve())