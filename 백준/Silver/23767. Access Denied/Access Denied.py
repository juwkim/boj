import string

def solve():
    l = 1
    while True:
        print('a' * l, flush=True)
        s = input()
        if s == "ACCESS GRANTED":
            return
        if int(s[15:s.index(' ', 16)]) != 5:
            break
        l += 1
    chars = string.ascii_letters + string.digits
    ans = ['a'] * l
    for i in range(l):
        for c in chars:
            ans[i] = c
            print(''.join(ans), flush=True)
            s = input()
            if s == "ACCESS GRANTED":
                return
            if int(s[15:s.index(' ', 16)]) >= 23 + 9 * i:
                break
solve()