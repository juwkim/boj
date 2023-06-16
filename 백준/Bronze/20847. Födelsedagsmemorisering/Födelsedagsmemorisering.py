dic = {}
for _ in range(int(input())):
    name, c, day = input().split()
    c = int(c)
    if day in dic:
        dic[day] = max(dic[day], (c, name))
    else:
        dic[day] = (c, name)

names = sorted(val[1] for val in dic.values())
print(len(names))
for name in names:
    print(name)