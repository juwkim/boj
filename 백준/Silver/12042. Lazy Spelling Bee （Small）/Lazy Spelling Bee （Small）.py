mod = 10**9 + 7
for step in range(1, 1 + int(input())):
    s = input()
    if len(s) == 1:
        ans = 1
    else:
        ans = (1 + (s[0] != s[1])) * (1 + (s[-1] != s[-2]))
        for i in range(1, len(s) - 1):
            ans = (ans * len(set(s[i-1:i+2]))) % mod
    print(f'Case #{step}:', ans)