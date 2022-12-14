from collections import defaultdict
dic = defaultdict(int)
for _ in range(int(input())):
    dic[input()] += 1
name = max(dic, key=dic.get)
if 2 * dic[name] > sum(dic.values()):
    print(name)
else:
    print('NONE')