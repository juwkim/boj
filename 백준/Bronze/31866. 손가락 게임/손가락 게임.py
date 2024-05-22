def solve():
    a, b = map(int, input().split())
    if a == b:
        return "="
    if a in (0, 2, 5) and b in (0, 2, 5):
        if a == 0:
            return "<>"[b == 2]
        if a == 2:
            return "<>"[b == 5]
        return "<>"[b == 0]
    if a in (0, 2, 5):
        return ">"
    if b in (0, 2, 5):
        return "<"
    return "="
print(solve())