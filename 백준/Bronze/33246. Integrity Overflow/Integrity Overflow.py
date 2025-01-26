ans = "SYSTEM SECURE"
n = int(input())
password = input()
for _ in range(n):
    s, p = input().split()
    if (p[0] == "A") ^ (len(s) == len(password) and sum(a != b for a, b in zip(s, password)) < 2):
        ans = "INTEGRITY OVERFLOW"
        break
print(ans)