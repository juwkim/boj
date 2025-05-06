s = input()
def solve(s, c):
    ret, l = 0, []
    for i in range(len(s)):
        if s[i] == c:
            ret += len(l)
        else:
            l.append(s[i])
    return ret, l

ret1, l = solve(s, '0')
ret2, l = solve(l, '1')
print(ret1 + ret2)