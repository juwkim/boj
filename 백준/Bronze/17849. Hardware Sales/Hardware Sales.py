from collections import Counter
g = lambda: [*map(int, input().split())]

nums = g()
items = [[], [], []]
for i in range(3):
    while len(items[i]) != 2 * nums[i]:
        items[i] += input().split()
dic = [Counter() for _ in range(3)]
for i in range(3):
    for j in range(0, len(items[i]), 2):
        k, v = items[i][j], items[i][j+1]
        if dic[i].get(k):
            dic[i][k] += int(v)
        else:
            dic[i][k] = int(v)
a = dic[0] & dic[1] & dic[2]
res = sorted([k for k, v in a.items() if v >= 20], key=lambda x: list(dic[0].keys()).index(x))
print(len(res), *res)