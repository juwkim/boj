from collections import defaultdict
dic = defaultdict(int)
for _ in range(int(input())):
    dic[int(input())] += 1
print(max(dic, key=lambda x: (dic[x], -x)))