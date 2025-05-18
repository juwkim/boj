def solve(c):
    i, j = s.find(c), s.rfind(c)
    if i == -1 or i == j:
        return -1, -1
    return i + 1, j, i + 2, j + 1
s = input()
a, b = solve('0'), solve('1')
if a[0] == -1 and b[0] == -1:
    print(-1)
elif b[0] == -1:
    print(*a)
elif a[0] == -1:
    print(*b)
else:
    print(*max(a, b, key=lambda x: x[1] - x[0]))