ans = set()
for _ in range(int(input())):
    s, e = input().split('@')
    idx = s.find('+')
    if idx != -1:
        s = s[:idx]
    email = s.replace('.', '') + '@' + e
    ans.add(email)
print(len(ans))