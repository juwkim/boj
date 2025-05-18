def solve():
    seq = input()[::-1]
    if seq[0] != 'O' or "OO" in seq:
        return "INVALID"
    num = 16
    while True:
        cur = num
        for c in seq:
            if c == 'O':
                cur, r = divmod(cur - 1, 3)
                if r or cur & (cur - 1) == 0:
                    break
            else:
                cur <<= 1
        else:
            return cur
        num <<= 1
print(solve())