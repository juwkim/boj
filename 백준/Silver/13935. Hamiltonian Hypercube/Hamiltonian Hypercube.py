n, a, b = input().split()
n = int(n)
def solve(s):
    ret, num, f = 0, 1 << n - 1, True
    for c in s:
        if (c == '0') ^ f: ret += num
        f ^= c == '1'
        num >>= 1
    return ret
print(solve(b) - solve(a) - 1)