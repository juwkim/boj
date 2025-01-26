import sys
input = lambda: sys.stdin.readline().rstrip()

ans = "SYSTEM SECURE"
n = int(input())
password = input()
for _ in range(n):
    s, p = input().split()
    if p == "ALLOWED":
        if len(s) != len(password) or sum(a != b for a, b in zip(s, password)) > 1:
            ans = "INTEGRITY OVERFLOW"
            break
    else:
        if len(s) == len(password) and sum(a != b for a, b in zip(s, password)) <= 1:
            ans = "INTEGRITY OVERFLOW"
            break
print(ans)