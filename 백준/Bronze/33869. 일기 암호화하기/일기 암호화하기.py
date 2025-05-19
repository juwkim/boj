W = input()
check = set()
l = []
for c in W:
    if c not in check:
        l.append(c)
        check.add(c)
dic = {chr(65 + i): l[i] for i in range(len(l))}
j = 65
for i in range(len(l), 26):
    while chr(j) in check:
        j += 1
    dic[chr(65 + i)] = chr(j)
    j += 1
print("".join(dic[c] for c in input()))