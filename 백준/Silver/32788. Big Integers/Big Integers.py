import sys
input = lambda: sys.stdin.readline().rstrip()

def solve():
    if len(a) > len(b):
        return True
    if len(a) < len(b):
        return False
    for p, q in zip(a, b):
        if p == q:
            continue
        if p.isdigit():
            if p > q:
                return True
            return False
        elif p.isupper():
            if q.islower() or p > q:
                return True
            return False
        elif q.isupper():
            return False
        elif p > q:
            return True
        return False

for _ in range(int(input())):
    a, b = input(), input()
    if (a > b and solve()) or (a < b and not solve()):
        print("YES")
    else:
        print("NO")