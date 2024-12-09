import sys
input = sys.stdin.readline

def solve(s):
    h, m = map(int, s.split(':'))
    d = h % 12 * 30 - m * 5.5
    return min(d % 360, -d % 360), s

for _ in range(int(input())):
    print(sorted(input().split(), key=solve)[2])