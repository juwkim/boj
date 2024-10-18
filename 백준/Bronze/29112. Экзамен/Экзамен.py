l, r = map(int, input().split())

def solve(num):
    if num < 0:
        return 0
    return int((num // 36000) ** (1/6) + 1e-12) + 1

print(solve(r) - solve(l - 1))