import sys
input = lambda: sys.stdin.readline().rstrip()

for _ in range(int(input())):
    ans = []
    s = input()
    prev = 0
    for i in range(1, len(s)):
        if s[i].isupper():
            ans.append(s[prev:i].lower())
            prev = i
    ans.append(s[prev:].lower())
    print(*ans, sep='_')