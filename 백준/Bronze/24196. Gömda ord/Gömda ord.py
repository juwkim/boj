s = input()
idx = 0
ans = []
while idx < len(s):
    ans.append(s[idx])
    idx += ord(s[idx]) - 64
print(*ans, sep='')