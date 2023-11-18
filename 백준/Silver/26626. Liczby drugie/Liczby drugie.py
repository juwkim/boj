import sys
input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5)+1):
        if not num % i:
            return False
    return True

def solve(s):
    for i in range(1, len(s)):
        if s[i] == '0':
            continue
        a, b = int(s[:i]), int(s[i:])
        if is_prime(a) and is_prime(b):
            return "TAK"
    return "NIE"

print(solve(input()))