import sys
input = lambda: sys.stdin.readline().rstrip()

dic = {chr(i): [] for i in range(97, 123)}

c = input()[-1]
for _ in range(int(input())):
    s = input()
    dic[s[0]].append(s)

ans = True
if len(dic[c]):
    for animal in dic[c]:
        p = animal[-1]
        if len(dic[p]) <= (c == p):
            ans = animal + '!'
            break
    if ans == True:
        ans = dic[c][0]
else:
    ans = '?'
print(ans)