import sys
input = sys.stdin.readline
table = {} 
for _ in range(int(input())):
    s = input()
    before, after = s[0], s[2]
    table[before] = after

ans = ""
for _ in range(int(input())):
    s = input()[0]
    if s in table:
        ans += table[s]
    else:
        ans += s
print(ans)