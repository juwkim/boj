import sys
input = lambda: sys.stdin.readline().rstrip()
ans, check = 0, set()
for _ in range(int(input())):
    s = input()
    if s == 'ENTER':
        ans += len(check)
        check = set()
    else:
        check.add(s)
ans += len(check)
print(ans)