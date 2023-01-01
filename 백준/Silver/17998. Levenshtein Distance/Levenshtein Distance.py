p = input()
s = input()
ans = set()
for c in p:
    for i in range(len(s) + 1):
        ans.add(s[:i] + c + s[i:])
    for i in range(len(s)):
        ans.add(s[:i] + c + s[i + 1:])

for i in range(len(s)):
    ans.add(s[:i] + s[i + 1:])

if s in ans:
    ans.remove(s)

for word in sorted(ans):
    print(word)