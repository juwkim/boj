n = int(input())
cypher = input()
ans = [input()]
for c in cypher[-1:0:-1]:
    ans.append(chr((ord(c) - ord(ans[-1])) % 26 + 97))
print(*ans[::-1], sep='')