import sys
input = lambda: sys.stdin.readline().rstrip()

n, m = map(int, input().split())
if all(input().count('A') == 1 for _ in range(n)):
    print("Yes")
else:
    print("No")