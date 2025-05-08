input()
ans = 0
for M in sorted(map(int, input().split())):
    if M > ans + 1:
        break
    ans += M
print(ans + 1)