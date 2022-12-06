from collections import defaultdict
dic = defaultdict(int)
for _ in range(int(input())):
    dic[input()] += 1
print(min(dic, key=lambda x: (-dic[x], x)))