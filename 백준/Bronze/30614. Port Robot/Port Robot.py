def solve():
    l = []
    for c in input():
        if c.islower():
            l.append(c)
        elif l and c.lower() == l[-1]:
            l.pop()
        else:
            return 0
    return +(len(l) == 0)
input()
print(solve())