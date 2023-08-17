n = int(input())
l = [input() for _ in range(n)]
i = l.index("?")

if i > 0:
    s = l[i - 1][-1]
else:
    s = ""
if i < n - 1:
    e = l[i + 1][0]
else:
    e = ""
sl = set(l)
for _ in range(int(input())):
    word = input()
    if word in sl:
        continue
    if word.startswith(s) and word.endswith(e):
        print(word)
        break