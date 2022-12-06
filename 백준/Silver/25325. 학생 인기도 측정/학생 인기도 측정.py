n = int(input())
names = input().split()
dic = {name: 0 for name in names}

for i in range(n):
    for name in input().split():
        dic[name] += 1

for key, val in sorted(dic.items(), key=lambda x: (-x[1], x[0])):
    print(key, val)