def solve(c):
    i, j = s.find(c), s.rfind(c)
    if i == -1 or i == j:
        return -1, -1
    p = s[i: j + 1]
    assert s.find(p) == i and s.rfind(p) == i
    return i + 1, j, i + 2, j + 1
s = input()
a, b = solve('0'), solve('1')
if a[0] == -1 and b[0] == -1:
    print(-1)
elif b[0] == -1 or (a[1] - a[0] > b[1] - b[0]) or (a[1] - a[0] == b[1] - b[0] and a[0] > b[0]):
    print(*a)
else:
    print(*b)