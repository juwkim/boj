from collections import defaultdict
dic = defaultdict(int)
for _ in range(int(input())):
    dic[input().split('.')[1]] += 1
for k in sorted(dic):
    print(k, dic[k])