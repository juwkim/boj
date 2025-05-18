import sys
input = lambda: sys.stdin.readline().rstrip()

for _ in range(int(input())):
    n = int(input())
    s = input()
    if s[0] == 'L' and s[-1] == 'R':
        print("NO")
    else:
        print("YES")