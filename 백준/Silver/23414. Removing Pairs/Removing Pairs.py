def solve():
    s, t = input(), input()
    i, j = 0, 0
    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            i += 1
            j += 1
        else:
            j += 2
    if i == len(s) and (j - len(t)) % 2 == 0:
        return "YES"
    return "NO"
print(solve())