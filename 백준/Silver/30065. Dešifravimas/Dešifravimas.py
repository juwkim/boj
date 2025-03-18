M = int(input())
a, b = input(), input()
for s, t in zip(a, b):
    if s == t:
        continue
    K = (ord(t) - ord(s)) % 26
ans = []
for c in b:
    if c.isalpha():
        if c.islower():
            ans.append(chr((ord(c) - ord('a') - K) % 26 + ord('a')))
        else:
            ans.append(chr((ord(c) - ord('A') - K) % 26 + ord('A')))
    else:
        ans.append(c)
print(*ans, sep='')