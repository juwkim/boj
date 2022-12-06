ans = set()
for _ in range(int(input())):
    s = input()
    l = len(s)
    s += s
    if all(s[i:i+l] not in ans for i in range(l)):
        ans.add(s[:l])
print(len(ans))