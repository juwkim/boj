def solve():
    s, t = input(), input()
    i, j = len(s) - 1, len(t) - 1
    while i >= 0 and j >= 0:
        if s[i] == t[j]:
            i -= 1
            j -= 1
        else:
            j -= 2
    if i == -1 and j & 1:
        return "YES"
    return "NO"
print(solve())