import sys
input = lambda: sys.stdin.readline().rstrip()

for tc in range(1, 1 + int(input())):
    num = int(input())
    ans = 0
    for a in range(num + 1):
        b = num - a
        ans = max(ans, a.bit_count() + b.bit_count())
    print(f"Case #{tc}: {ans}")