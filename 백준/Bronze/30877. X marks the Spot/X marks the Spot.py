ans = []
for _ in range(int(input())):
    s, t = input().split()
    ans.append(t[s.upper().index('X')].upper())
print(*ans, sep='')