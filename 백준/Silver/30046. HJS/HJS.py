import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

def solve():
    N = int(input())
    P, Q, R = input(), input(), input()
    check = set()
    for a, b in zip(P, Q):
        if a != b:
            check.add(a + b)
            break
    else:
        return "Hmm..."
    for b, c in zip(Q, R):
        if b != c:
            if c + b in check:
                return "Hmm..."
            check.add(b + c)
            break
    else:
        return "Hmm..."
    for a, c in zip(P, R):
        if a != c:
            if c + a in check:
                return "Hmm..."
            break
    else:
        return "Hmm..."
    return "HJS! HJS! HJS!"

print(solve())